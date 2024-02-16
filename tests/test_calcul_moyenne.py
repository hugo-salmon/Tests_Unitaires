import unittest
from functions import calcul_moyenne

class TestCalculerMoyenne(unittest.TestCase):
    """
    Classe de test pour la fonction calcul_moyenne
    """

    def test_moyenne(self):
        """
        Vérifie si la moyenne est correctement calculée pour une liste non vide
        """
        self.assertEqual(calcul_moyenne([10, 20, 30, 40, 50]), 30)

    def test_moyenne_liste_vide(self):
        """
        Vérifie si une erreur ValueError est levée lorsque la liste est vide
        """
        with self.assertRaises(ValueError):
            calcul_moyenne([])

    def test_moyenne_un_seul_element(self):
        """
        Vérifie si la moyenne est correctement calculée pour une liste avec un seul élément
        """
        self.assertEqual(calcul_moyenne([20]), 20)

    def test_moyenne_negatifs(self):
        """
        Vérifie si la moyenne est correctement calculée pour une liste de nombres négatifs
        """
        self.assertEqual(calcul_moyenne([-10, -20, -30, -40, -50]), -30)

    def test_moyenne_decimaux(self):
        """
        Vérifie si la moyenne est correctement calculée pour une liste de nombres décimaux
        """
        self.assertAlmostEqual(calcul_moyenne([1.5, 2.5, 3.5]), 2.5)

if __name__ == '__main__':
    unittest.main()