# Fonctions
def Moyenne_arithmetique(echantillon: list) -> float:
    return sum(echantillon) / len(echantillon)

def Calcul_moment_centré_ordre_k(echantillon: list, k: int) -> float:
    m = Moyenne_arithmetique(echantillon)
    return sum((x - m)**k for x in echantillon) / len(echantillon)

def Calcul_Skewness_Pearson(echantillon: list) -> float:
    return Calcul_moment_centré_ordre_k(echantillon, 3)**2 / Calcul_moment_centré_ordre_k(echantillon, 2)**3

def Calcul_Kurtosis_Pearson(echantillon: list) -> float:
    return Calcul_moment_centré_ordre_k(echantillon, 4) / Calcul_moment_centré_ordre_k(echantillon, 2)**2

# Définition des variables
echantillon = [25, 43, 35, 20, 32, 30, 35, 24, 45]

# Affichage
print("Artithmetique : ", Moyenne_arithmetique(echantillon))

for k in range(3):
    print(f"moment centré {k} : ", Calcul_moment_centré_ordre_k(echantillon, k))

print("Asymétrie Pearson : ", Calcul_Skewness_Pearson(echantillon))

print("Aplatissement Pearson : ", Calcul_Kurtosis_Pearson(echantillon))
