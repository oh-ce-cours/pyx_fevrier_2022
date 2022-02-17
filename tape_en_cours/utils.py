def traitement_cellule(element):
    element_sans_espace = element.strip()  # on enleve les espaces
    try:
        element_transforme = float(1 / int(element_sans_espace)) ** 2
        element_au_carre = f"{element_transforme:.2f}"
    except ValueError:
        element_au_carre = "NA"
    except ArithmeticError as e:
        print("On a un 0, on ne devrait pas", e, type(e))
        element_au_carre = "NaN"

    return f"{element_au_carre:>8}"
