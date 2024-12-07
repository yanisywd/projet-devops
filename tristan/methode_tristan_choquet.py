def methode1tchoquet(a, b, c):
    if a == 0:
        raise ZeroDivisionError
    if a < 0:
        raise ValueError
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        raise TypeError
    # Calcul de la moyenne
    moyenne = (a + b + c) / 3
    # Calcul de la somme
    somme = a + b + c
    # Calcul du produit
    produit = a * b * c
    # Calcul de la différence
    difference = a - b - c
    # Calcul de la racine carrée
    racine = a ** (1/2)
    # Calcul du carré
    carre = a ** 2
    # Calcul du cube
    cube = a ** 3
    # Calcul de l'inverse
    inverse = 1 / a
    # Calcul de l'opposé
    oppose = -a

    return moyenne, somme, produit, difference, racine, carre, cube, inverse, oppose

def methode2tchoquet(text1, text2):
    if not isinstance(text1, str) or not isinstance(text2, str):
        raise TypeError
    if text1 == "" or text2 == "":
        raise AssertionError
    # Calcul de la longueur des textes
    longueur_text1 = len(text1)
    longueur_text2 = len(text2)
    # Calcul de la concaténation des textes
    concatenation = text1 + text2
    # Calcul de la répétition des textes
    repetition = text1 * 3 + text2 * 2
    # Calcul de la liste des caractères des textes
    liste_text1 = list(text1)
    liste_text2 = list(text2)
    # Calcul de la liste des mots des textes
    liste_mots_text1 = text1.split()
    liste_mots_text2 = text2.split()
    # Calcul de la liste des phrases des textes
    liste_phrases_text1 = text1.split('.')
    liste_phrases_text2 = text2.split('.')
    # Calcul de la liste des lignes des textes
    liste_lignes_text1 = text1.split('\n')
    liste_lignes_text2 = text2.split('\n')

    return longueur_text1, longueur_text2, concatenation, repetition, liste_text1, liste_text2, liste_mots_text1, liste_mots_text2, liste_phrases_text1, liste_phrases_text2, liste_lignes_text1, liste_lignes_text2