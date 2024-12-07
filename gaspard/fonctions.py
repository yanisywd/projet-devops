from typing import List

type_echantillon = List[int]

# Fonctions
def Moyenne_arithmetique(echantillon: type_echantillon) -> float:
    assert len(echantillon) > 0, "L'échantillon ne doit pas être vide"
    assert all(isinstance(x, int) for x in echantillon), "Les éléments de l'échantillon doivent être des entiers"
    res = sum(echantillon) / len(echantillon)
    assert res >= min(echantillon), "Le résultat doit être supérieur au plus petit élément de la liste"
    assert res <= max(echantillon), "Le résultat doit être inférieur au plus grand élément de la liste"
    return res

def Calcul_moment_centré_ordre_k(echantillon: type_echantillon, k: int) -> float:
    assert len(echantillon) > 0, "L'échantillon ne doit pas être vide"
    assert all(isinstance(x, int) for x in echantillon), "Les éléments de l'échantillon doivent être des entiers"
    m = Moyenne_arithmetique(echantillon)
    return sum((x - m)**k for x in echantillon) / len(echantillon)

def Calcul_Skewness_Pearson(echantillon: type_echantillon) -> float:
    assert len(echantillon) > 0, "L'échantillon ne doit pas être vide"
    assert all(isinstance(x, int) for x in echantillon), "Les éléments de l'échantillon doivent être des entiers"
    return Calcul_moment_centré_ordre_k(echantillon, 3)**2 / Calcul_moment_centré_ordre_k(echantillon, 2)**3

def Calcul_Kurtosis_Pearson(echantillon: type_echantillon) -> float:
    assert len(echantillon) > 0, "L'échantillon ne doit pas être vide"
    assert all(isinstance(x, int) for x in echantillon), "Les éléments de l'échantillon doivent être des entiers"
    return Calcul_moment_centré_ordre_k(echantillon, 4) / Calcul_moment_centré_ordre_k(echantillon, 2)**2
