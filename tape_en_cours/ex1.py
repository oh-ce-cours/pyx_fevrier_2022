# from utils import traitement_cellule
# traitement_cellule()

# import utils 
# utils.traitement_cellule()

import time 
# on veut transformer un "CSV séparé par des lignes" en 
# "CSV avec des largeurs de colonnes fixes (5 chars) en mettant au carré chacun des éléments" 
ligne = "  1,   2   ,3,4,5 \n ,  toto, 7, 9, 10, 11"
datas = ligne.split(",")

data_sans_espaces = []
for element in datas:
    try:
        time.sleep(0.5)
    except Exception: 
        print("on sort pas")

    element_sans_espace = element.strip()  # on enleve les espaces
    try:
        element_au_carre = str(int(element_sans_espace) ** 2)
    except ValueError:
        element_au_carre = "NA"
    data_sans_espaces.append(element_au_carre)

    ## différentes méthodes d'affichage, par affinité avec le formateur 
    ## elles font toutes la même chose
    print(f"'{element_au_carre}'")
    # print("'{}'".format(element_sans_espace))
    # print("'%s'" % (element_sans_espace,))
    # print("'" + str(element_sans_espace) + "'")