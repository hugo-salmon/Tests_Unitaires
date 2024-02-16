import unittest
from functions import est_premier

class TestEstPremier(unittest.TestCase):
    """
    Classe de test pour la fonction est_premier
    """

    def test_nombres_negatifs(self):
        """
        Vérifie si des nombres négatifs retournent correctement False
        """
        self.assertFalse(est_premier(-10))
        self.assertFalse(est_premier(-50))
        self.assertFalse(est_premier(-200))

    def test_zero_et_un(self):
        """
        Vérifie si 0 et 1 retournent correctement False
        """
        self.assertFalse(est_premier(0))
        self.assertFalse(est_premier(1))

    def test_nombres_non_premiers(self):
        """
        Vérifie si des nombres non premiers retournent correctement False
        """
        self.assertFalse(est_premier(4))
        self.assertFalse(est_premier(6))
        self.assertFalse(est_premier(8))
        self.assertFalse(est_premier(10))

    def test_nombres_premiers(self):
        """
        Vérifie si des nombres premiers retournent correctement True
        """
        self.assertTrue(est_premier(2))
        self.assertTrue(est_premier(3))
        self.assertTrue(est_premier(7))
        self.assertTrue(est_premier(11))
        self.assertTrue(est_premier(17))

    def test_grands_nombres(self):
        """
        Vérifie si des grands nombres retournent correctement True ou False
        """
        self.assertTrue(est_premier(22091))  # Nombre premier
        self.assertFalse(est_premier(22092))  # Nombre non premier

if __name__ == '__main__':
    unittest.main()
