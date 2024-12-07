from tests_unitaires import test
from fonctions import Moyenne_arithmetique, Calcul_moment_centré_ordre_k, Calcul_Skewness_Pearson, Calcul_Kurtosis_Pearson

if __name__ == "__main__":
    if not test():
        raise Exception("Les tests ont échoué")
        