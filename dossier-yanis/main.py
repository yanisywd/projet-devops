# Yahia Ouahmed Yanis

class Panier:
    def __init__(self):
        self.articles = []
        self.remise = 0
        self.taxe = 0.2  # Taxe de 20%

    def ajouter_article(self, nom, prix):
        """Ajoute un article au panier"""
        self.articles.append({"nom": nom, "prix": prix})

    def appliquer_remise(self, pourcentage):
        """Applique une remise en pourcentage sur le total du panier"""
        self.remise = pourcentage

    def calculer_total(self):
        """Calcule le total du panier après remise et taxe"""
        total_sans_remise = sum(article["prix"] for article in self.articles)
        total_apres_remise = total_sans_remise * (1 - self.remise / 100)
        total_avec_taxe = total_apres_remise * (1 + self.taxe)
        return total_avec_taxe

    def afficher_panier(self):
        """Affiche le contenu du panier"""
        return [{"nom": article["nom"], "prix": article["prix"]} for article in self.articles]



#TEST UNITAIRES

import unittest
class TestPanier(unittest.TestCase):

    def setUp(self):
        """Methode appelée avant chaque test """
        self.panier = Panier()

    def test_ajouter_article(self):
        """Test l'ajout d'articles dans le panier"""
        self.panier.ajouter_article("Pomme", 2.5)
        self.assertEqual(len(self.panier.articles), 1)
        self.assertEqual(self.panier.articles[0]["nom"], "Pomme")
        self.assertEqual(self.panier.articles[0]["prix"], 2.5)
        print("Test 'test_ajouter_article' passé avec succès ✅")

    def test_appliquer_remise(self):
        """Test l'application de remise"""
        self.panier.ajouter_article("Pomme", 2.5)
        self.panier.ajouter_article("Banane", 1.5)
        self.panier.appliquer_remise(10)
        total_attendu = (2.5 + 1.5) * 0.9 * 1.2  # Remise de 10% et taxe de 20%
        self.assertAlmostEqual(self.panier.calculer_total(), total_attendu)
        print("Test 'test_appliquer_remise' passé avec succès ✅")

    def test_calculer_total_sans_remise(self):
        """Test du calcul du total sans remise"""
        self.panier.ajouter_article("Pomme", 2.5)
        self.panier.ajouter_article("Banane", 1.5)
        total_sans_remise = 2.5 + 1.5
        total_attendu = total_sans_remise * 1.2  # Taxe de 20%
        self.assertAlmostEqual(self.panier.calculer_total(), total_attendu)
        print("Test 'test_calculer_total_sans_remise' passé avec succès ✅")

    def test_calculer_total_avec_remise_et_taxe(self):
        """Test du calcul du total avec remise et taxe"""
        self.panier.ajouter_article("Pomme", 2.5)
        self.panier.ajouter_article("Banane", 1.5)
        self.panier.appliquer_remise(10)  # Remise de 10%
        total_sans_remise = 2.5 + 1.5
        total_apres_remise = total_sans_remise * 0.9
        total_attendu = total_apres_remise * 1.2  # Taxe de 20%
        self.assertAlmostEqual(self.panier.calculer_total(), total_attendu)
        print("Test 'test_calculer_total_avec_remise_et_taxe' passé avec succès ✅")

    def test_afficher_panier(self):
        """Test de l'affichage des articles du panier"""
        self.panier.ajouter_article("Pomme", 2.5)
        self.panier.ajouter_article("Banane", 1.5)
        panier_attendu = [{"nom": "Pomme", "prix": 2.5}, {"nom": "Banane", "prix": 1.5}]
        self.assertEqual(self.panier.afficher_panier(), panier_attendu)
        print("Test 'test_afficher_panier' passé avec succès ✅")


if __name__ == '__main__':
    unittest.main()




# Voici quelque scenerio en Gherkin pour Pour intégrer des tests BDD
# je n'ai pas eu assez de temps pour les coder


# Feature: Gestion du panier d'achat
#   En tant qu'utilisateur, je veux pouvoir ajouter des articles, appliquer des remises et calculer le total afin de gérer mes achats.

#   Scenario: Ajouter un article au panier
#     Given un panier vide
#     When j'ajoute un article "Pomme" à 2.5 euros
#     Then le panier contient 1 article
#     And le total du panier est 3.0 euros (avec taxes)

#   Scenario: Appliquer une remise
#     Given un panier avec les articles suivants:
#       | nom   | prix |
#       | Pomme | 2.5  |
#       | Banane| 1.5  |
#     When j'applique une remise de 10%
#     Then le total du panier est 3.6 euros (avec taxes)

#   Scenario: Calculer le total sans remise
#     Given un panier avec les articles suivants:
#       | nom   | prix |
#       | Pomme | 2.5  |
#       | Banane| 1.5  |
#     When je calcule le total sans remise
#     Then le total du panier est 4.8 euros (avec taxes)

#   Scenario: Afficher les articles du panier
#     Given un panier avec les articles suivants:
#       | nom   | prix |
#       | Pomme | 2.5  |
#       | Banane| 1.5  |
#     When je demande la liste des articles
#     Then la liste des articles est:
#       | nom   | prix |
#       | Pomme | 2.5  |
#       | Banane| 1.5  |
