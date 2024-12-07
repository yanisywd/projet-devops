from fonctions import Moyenne_arithmetique, Calcul_moment_centré_ordre_k, Calcul_Skewness_Pearson, Calcul_Kurtosis_Pearson
from typing import List

type_echantillon = List[int]


# Providers et tests unitatires
provider_Moyenne_arithmetique= [
    ([37, 68, 74, 9, 62, 42, 94, 5, 54, 60, 33, 3, 48, 24, 100, 34, 67, 32, 76], 48.526315789473685),
    ([37, 68, 74, 9, 62, 42, 94, 5, 54, 60, 33, 3, 48, 24, 100, 34, 67, 32, 76], 48.53),
    ([25, 5, 99, 42, 66, 8, 62, 83, 17, 32, 49, 60, 61, 12, 33, 76, 57, 72, 16, 21, 91, 69, 27, 29, 35, 80, 30, 75, 73, 46, 15, 78, 43, 71, 38, 54, 92, 19, 55, 70, 85, 63, 50, 39, 81, 14, 45, 96, 86, 4, 48, 22, 9, 59, 31, 28, 82, 37, 41, 79, 58, 67, 93, 7, 40, 84, 87, 47, 44, 52, 88, 77, 34, 26, 68, 51, 74, 24, 56, 6, 36, 90, 11, 23, 2, 3, 53, 13, 18, 64, 65], 48.86)
]

def test_Moyenne_arithmetique(echantillon: type_echantillon, res: float) -> bool:
    return Moyenne_arithmetique(echantillon) == res

provider_Calcul_moment_centré_ordre_k = [
    ([27, 69, 56, 2, 71, 55, 8, 91, 45, 51, 92, 93, 54, 10, 76, 40, 75, 38, 50, 99, 74, 7, 26, 79, 24, 90, 48, 42, 72, 44, 11, 53, 70, 12, 88, 41, 66, 37, 32, 81, 67, 20, 61, 58, 78, 4, 60, 6, 22, 5, 82, 17], 2, 786.1638313609467),
    ([48, 99, 82, 31, 27, 91, 24, 19, 43, 14, 39, 94, 89, 95, 42, 9, 12, 25, 18, 59, 33, 20, 15, 36, 60, 72, 85, 51, 8, 44, 90, 54, 1, 35, 7, 83, 98, 26, 53, 70, 78, 46, 41, 58, 76, 62, 32, 38, 11, 74, 10, 68, 56, 22, 13, 50, 49, 67, 61, 96, 75, 16, 2, 3, 5, 47, 93, 17, 71, 55, 30, 88, 86, 66, 63, 45, 69, 87, 37, 52, 65, 40, 29, 79, 100, 80, 6, 28, 4, 57, 23, 97, 73, 64, 21, 92, 84, 77, 81], 2, 838.8888888888891),
    ([57, 69, 30, 87, 49, 9, 62, 94, 5, 21, 48, 91, 96, 6, 85, 75, 42, 33, 79, 10, 13, 29, 34, 70, 44, 12, 40, 74, 4, 86, 63, 3, 23, 76, 14, 72, 15, 58, 95, 92, 31, 36, 41, 83, 71, 73, 80, 55, 67], 2, 851.4044148271554),
]

def test_Calcul_moment_centré_ordre_k(echantillon: type_echantillon, k: int, res: float) -> bool:
    return Calcul_moment_centré_ordre_k(echantillon, k) == res

provider_Calcul_Skewness_Pearson = [
    ([5, 41, 81, 55, 65, 90, 99, 94, 29, 13, 83, 98, 60, 10, 67, 17, 47, 8, 16, 44, 63, 62, 9, 40, 25, 14, 37, 73, 3, 34, 68, 72, 23, 22, 1, 24, 18, 66, 36, 53, 77, 74, 86, 19, 32, 71, 52, 95, 89, 91, 46, 100, 49, 28, 39, 27, 87, 51, 75, 56, 31, 11, 7, 33, 58, 70, 92, 78, 26, 45, 69, 20, 85, 50, 6, 97, 61, 93, 80, 42, 43, 82, 35, 12, 96, 84, 15, 4, 30, 2, 48, 88, 64], 3, 0.027917194941615976),
    ([76, 1, 21, 10, 63, 59, 74, 53, 80, 66, 56, 25, 79, 87, 5, 7, 45, 29, 40, 83, 13, 57, 3, 31, 4, 70, 44, 86, 41, 30, 89, 58, 72], 3, -0.20150855342259819),
    ([24, 44, 45, 53, 46, 16, 92, 98, 41, 1, 77, 11, 55, 38, 56, 19, 12, 59, 86, 62, 40, 4, 49, 65, 23, 30, 54, 32, 69, 34, 94, 93, 82, 20, 17, 78, 21, 60, 64, 96, 71, 5, 15, 52, 9, 37, 89, 3, 26, 36, 91, 28, 10, 50, 58, 99, 81, 87, 61, 33, 31, 75, 67, 72, 42, 80, 2, 43, 97, 22, 6], 3, 0.11078110190906533),
]

def test_Calcul_Skewness_Pearson(echantillon: type_echantillon, res: float) -> bool:
    return Calcul_Skewness_Pearson(echantillon) == res

provider_Calcul_Kurtosis_Pearson = [
    ([56, 14, 47, 72, 19, 76, 27, 22, 40, 88, 13, 33, 77, 95, 52], 4, -1.285232156006837),
    ([68, 27, 52, 55, 15, 84, 13, 10, 100, 22, 19, 98, 75, 41, 93, 62, 86, 25, 65, 31, 12, 83, 4, 60, 48, 20, 97, 74, 54, 70, 8, 23, 5, 59, 35, 85, 18, 42, 46, 87, 91, 89, 90, 24, 94, 63, 96, 79, 53, 2, 82, 50, 40, 29, 45, 16, 67, 38, 11, 56, 33, 6, 1, 32, 44, 72, 36, 80, 47, 58, 51, 66, 21, 78, 39, 92, 26], 4, -1.1915851618717164),
    ([29, 91, 90, 47, 19, 89, 57, 51, 42, 17, 78, 52, 61, 39, 96, 37, 4, 88, 63, 12, 86, 28], 4, -1.217704077044095),
]

def test_Calcul_Kurtosis_Pearson(echantillon: type_echantillon, res: float) -> bool:
    return Calcul_Kurtosis_Pearson(echantillon) == res

# Méthode pour lancer tous les tests
def test() -> bool:
    for _ in provider_Moyenne_arithmetique:
        if not test_Moyenne_arithmetique(_[0], _[1]):
            return "Erreur dans la méthode Moyenne_arithmetique"
        
    for _ in provider_Calcul_moment_centré_ordre_k:
        if not test_Calcul_moment_centré_ordre_k(_[0], _[1], _[2]):
            return "Erreur dans la méthode Calcul_moment_centré_ordre_k"
        
    for _ in provider_Calcul_Skewness_Pearson:
        if not test_Calcul_Skewness_Pearson(_[0], _[1]):
            return "Erreur dans la méthode Calcul_Skewness_Pearson"
        
    for _ in provider_Calcul_Kurtosis_Pearson:
        if not test_Calcul_Kurtosis_Pearson(_[0], _[1]):
            return "Erreur dans la méthode Calcul_Kurtosis_Pearson"