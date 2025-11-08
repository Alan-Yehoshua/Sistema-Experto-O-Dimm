import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import _tree

## CARGAMOS EL DATASET Y APLICAMOS UNA NORMALIZACION EN ALGUNOS ATRIBUTOS
DATASET_PATH = "games_characters.csv"
df = pd.read_csv(DATASET_PATH, encoding="latin1")
df = df.rename(columns={"Genre_AcciÃ³n": "Genre_Accion",
                        "Un jugador":"Un_jugador",
                        "Genre_Multijugador masivo":"Genre_Multijugador_masivo"})


## ESCOGEMOS LOS ATRIBUTOS PARA EL ARBOL
cols = [
    'Name', 'Is_free', 'Is_PVP', 'Gano_GOTY',
    'Genre_Accion', 'Genre_Aventura', 'Genre_Carreras',
    'Genre_Casual', 'Genre_Deportes', 'Genre_Estrategia',
    'Genre_Indie', 'Mixed', 'Multijugador', 'Un_jugador',
    'Genre_Multijugador_masivo', 'Genre_Rol', 'Genre_Simuladores'
]
df = df[cols].dropna()

##  PREPARAMOS LAS VARIABLES PARA EL DATASET
X = df.drop(columns=['Name'])
y = df['Name']

y_le = LabelEncoder()
y_encoded = y_le.fit_transform(y) ## ETIQUETAMOS LOS VALORES DE NAME


## EMPEZAMOS CON EL ENTRENAMIENTO
clf = DecisionTreeClassifier(criterion='entropy', max_depth=8)
clf.fit(X, y_encoded)
print("Entrenamiento Terminado.\n")

## OBTENER REGLAS
def tree_to_pyknow_rules(clf, feature_names, class_names):
    tree_ = clf.tree_
    feature_name = [
        feature_names[i] if i != _tree.TREE_UNDEFINED else None
        for i in tree_.feature
    ]

    reglas_pyknow = []

    def recurse(node, condiciones):
        if tree_.feature[node] != _tree.TREE_UNDEFINED:
            name = feature_name[node]
            threshold = tree_.threshold[node]

            # Para variables binarias (0/1) → izquierda=no, derecha=sí
            cond_no = condiciones + [f'{name}="n"']
            cond_si = condiciones + [f'{name}="s"']

            recurse(tree_.children_left[node], cond_no)
            recurse(tree_.children_right[node], cond_si)
        else:
            clase = class_names[tree_.value[node].argmax()]
            if condiciones:  # evita reglas vacías
                regla = f"    @Rule(Juego({', '.join(condiciones)}))\n" \
                        f"    def regla_{len(reglas_pyknow)}(self):\n" \
                        f"        self.declare(Fact(resultado=\"{clase}\"))\n"
                reglas_pyknow.append(regla)

    recurse(0, [])
    return reglas_pyknow



## GENERAR ARCHIVO PYKNOW AUTOMÁTICO
reglas = tree_to_pyknow_rules(clf, X.columns, y_le.classes_)

header = '''
from pyknow import *

class Juego(Fact):
    pass

class GameExpert(KnowledgeEngine):
'''

footer = '''
    @Rule(Fact(resultado=MATCH.juego))
    def mostrar(self, juego):
        print(f"\\n El juego es: → {juego} ← ;)")


def obtener_respuesta(pregunta):
    ans = input(pregunta + " (s/n): ").strip().lower()
    while ans not in ["s", "n"]:
        ans = input("Responde solo con 's' o 'n': ").strip().lower()
    return ans


if __name__ == "__main__":
    print("Sistema Experto | O'Dimm")
    print("Piensa en un videojuego y responde las preguntas\\n")

    preguntas = {}
'''

# Generar preguntas dinámicamente
for col in X.columns:
    texto = col.replace("Genre_", "género ").replace("_", " ")
    footer += f'    preguntas["{col}"] = obtener_respuesta("¿El juego tiene {texto}?")\n'

footer += '''
    engine = GameExpert()
    engine.reset()
    engine.declare(Juego(**preguntas))
    engine.run()
    print("\\nFin del juego")
'''

with open("Juego_PyKnow.py", "w", encoding="utf-8") as f:
    f.write(header)
    for regla in reglas:
        f.write(regla + "\n")
    f.write(footer)

print(f"Archivo PyKnow generado con {len(reglas)} reglas.\n")