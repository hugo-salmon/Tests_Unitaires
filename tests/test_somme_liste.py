import unittest
from functions import somme_liste

class TestSommeListe(unittest.TestCase):
    """
    Classe de test pour la fonction somme_liste
    """

    def test_liste_vide(self):
        """
        Vérifie si la fonction retourne 0 pour une liste vide
        """
        self.assertEqual(somme_liste([]), 0)

    def test_liste_positifs(self):
        """
        Vérifie si la fonction retourne la somme correcte pour une liste de nombres positifs
        """
        self.assertEqual(somme_liste([1, 2, 4, 8, 10]), 25)

    def test_liste_negatifs(self):
        """
        Vérifie si la fonction retourne la somme correcte pour une liste de nombres négatifs
        """
        self.assertEqual(somme_liste([-1, -2, -4, -8, -10]), -25)

    def test_liste_mixte(self):
        """
        Vérifie si la fonction retourne la somme correcte pour une liste de nombres mixtes (positifs et négatifs)
        """
        self.assertEqual(somme_liste([-1, 2, -5, 8, -10]), -6)

    def test_liste_un_seul_element(self):
        """
        Vérifie si la fonction retourne le seul élément de la liste lorsqu'il y a un seul élément dans la liste
        """
        self.assertEqual(somme_liste([20]), 20)

if __name__ == '__main__':
    unittest.main()