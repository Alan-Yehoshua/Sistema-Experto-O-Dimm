import joblib
import numpy as np
from sklearn.tree import _tree

## CARGAMOS EL ID3
clf = joblib.load("arbol_entrenado.pkl")
y_le = joblib.load("encoder_y.pkl")

## CLASE  FUNCION DEL JUEGO
class Juego():
    ## LLAMAMOS LAS REGLAS Y LA PREDICCION DE JUEGOS
    def __init__(self, clf, y_le):
        super().__init__()
        self.clf = clf
        self.y_le = y_le

    ## INICIAMOS CON EL JUEGO
    def Jugar(self):
        print("==Sistema Experto: Adivina el juego | 0'Dimm ==")
        print("Piensa en un juego y responde con 's' o 'n' (minusculas).\n")

        ## OBTENEMOS LOS NOMBRES Y EL ARBOL
        tree = self.clf.tree_
        names = self.clf.feature_names_in_
        node = 0
        respuestas = {}

        ## COMENZAMOS A PREGUNTAR POR CADA NODO
        while tree.feature[node] != _tree.TREE_UNDEFINED:
            name = names[tree.feature[node]]

            # DEPENDIENDO EL NODO, ES LA PREGUNTA
            if name == "Is_free":
                pregunta = "¿El juego es Free to Play? (s/n): "
            elif name == "Is_PVP":
                pregunta = "¿Tiene modo PVP? (s/n): "
            elif name == "Gano_GOTY":
                pregunta = f"¿Gano a 'mejor juego del año'? (s/n): "
            elif name == "Multijugador" or name == "Un jugador" or name == "Mixed":
                pregunta = f"¿El modo de juego es {name}? (s/n): "
            elif name.startswith("Genre_"):
                q = name.replace("Genre_", "").replace("_", " ")
                pregunta = f"¿El juego pertenece al género {q}? (s/n): "
            else:
                pregunta = f"¿El juego tiene {name}? (s/n): "

            # GUARAMOS LA RESPUESTA Y VERIFCAMOS QUE SEA s O n
            ans = input(pregunta).strip().lower()
            while ans not in ["s", "n"]:
                ans = input("Responde solo con 's' o 'n': ").strip().lower()

            ## GUARDAMOS TODAS LAS RESPUESTAS PARA MOSTAR COMO LLEGAMOS A LA RESPUESTA
            respuestas[name] = ans

            ## NOS MOVEMOS ENTRE LOS NODOS SEGUN LA RESPUESTA
            node = tree.children_right[node] if ans == "s" else tree.children_left[node]

        # OBTENENMOS LA PREDICCION
        pred = np.argmax(tree.value[node])
        juego = self.y_le.classes_[pred]

        print(f"\n!!! El juego es: →{juego}← ;) !!!")

        # MOSTRAR RESPUESTAS
        print("\nRespuestas:")
        for k, v in respuestas.items():
            print(f"  - {k}: {'Sí' if v == 's' else 'No'}")

## MAIN
if __name__ == "__main__":
    game = Juego(clf, y_le)
    game.Jugar()