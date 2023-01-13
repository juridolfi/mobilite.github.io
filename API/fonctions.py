# fonctions utilis�es dans l API
import pandas as pd
import numpy as np

# FONCTION GENERALISTE


# Focntion qui � partir d'un data frame et d'un nom de colonne
#   retourne les valeurs de la colonne
#
#   @param  df   data frame
#   @param  colonne   string


def get_valeur_colonne(df, colonne):
    # recup�re les valeur d une colonne
    res = df[str(colonne)].value_counts()
    # liste o� les valeurs de la colonne sont stock�es
    x = []
    # boucle d'ajout des veleurs dans la structure finale
    for i in range(len(res)):
        col = str(res.keys()[i])
        x.append(col)

    data = {"data": x}

    return data

