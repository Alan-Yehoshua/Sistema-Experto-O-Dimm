import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import _tree
import joblib

## CARGAMOS EL DATASET Y APLICAMOS UNA NORMALIZACION EN ALGUNOS ATRIBUTOS
DATASET_PATH = "games_characters.csv"
df = pd.read_csv(DATASET_PATH, encoding="latin1")
df = df.rename(columns={"Genre_AcciÃ³n": "Genre_Accion"})

## ESCOGEMOS LOS ATRIBUTOS PARA EL ARBOL
cols = [
    'Name', 'Is_free', 'Is_PVP', 'Gano_GOTY',
    'Genre_Accion', 'Genre_Aventura', 'Genre_Carreras',
    'Genre_Casual', 'Genre_Deportes', 'Genre_Estrategia',
    'Genre_Indie', 'Mixed',  'Multijugador',  'Un jugador',
    'Genre_Multijugador masivo', 'Genre_Rol', 'Genre_Simuladores'
]
df = df[cols].dropna()

##  PREPARAMOS LAS VARIABLES PARA EL DATASET
X = df.drop(columns=['Name'])
y = df['Name']

y_le = LabelEncoder()
y_encoded = y_le.fit_transform(y) ## ETIQUETAMOS LOS VALORES DE NAME

## EMPEZAMOS CON EL ENTRENAMIENTO
clf = DecisionTreeClassifier(criterion='entropy', max_depth=15)
clf.fit(X, y_encoded)
print("Entrenamiento Terminado.\n")


## OBTENER REGLAS
def tree_to_rules(clf, feature_names, class_names):

    tree = clf.tree_
    feature_name = [
        feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
        for i in tree.feature
    ]
    rules = []

    def recurse(node, conditions):
        if tree.feature[node] != _tree.TREE_UNDEFINED:
            name = feature_name[node]
            threshold = tree.threshold[node]
            recurse(tree.children_left[node], conditions + [f"{name} <= {threshold:.2f}"])
            recurse(tree.children_right[node], conditions + [f"{name} > {threshold:.2f}"])
        else:
            class_val = class_names[tree.value[node].argmax()]
            rule = "IF " + " AND ".join(conditions) + f" THEN class = {class_val}"
            rules.append(rule)

    recurse(0, [])
    return rules


rules = tree_to_rules(clf, X.columns, y_le.classes_)

print("Reglas obtenidas:\n")
for r in rules:
    print(r)

print(f"\nTotal de reglas obtenidas: {len(rules)}\n")

## GUARDAMOS EL ARCHIVO
joblib.dump(clf, "arbol_entrenado.pkl")
joblib.dump(y_le, "encoder_y.pkl")

print("Modelo binario y reglas guardados correctamente.")