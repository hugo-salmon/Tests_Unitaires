import unittest
from functions import CompteBancaire

class TestCompteBancaire(unittest.TestCase):
    """
    Classe de test pour la classe CompteBancaire
    """

    def test_deposer(self):
        """
        Vérifie si la méthode deposer fonctionne correctement
        """
        compte = CompteBancaire(200)
        compte.deposer(100)
        self.assertEqual(compte.obtenir_solde(), 300)

    def test_retirer_solde_suffisant(self):
        """
        Vérifie si la méthode retirer fonctionne correctement avec un solde suffisant
        """
        compte = CompteBancaire(200)
        compte.retirer(50)
        self.assertEqual(compte.obtenir_solde(), 150)

    def test_retirer_solde_insuffisant(self):
        """
        Vérifie si la méthode retirer génère une erreur en cas de solde insuffisant
        """
        compte = CompteBancaire(200)
        with self.assertRaises(ValueError):
            compte.retirer(250)

    def test_obtenir_solde(self):
        """
        Vérifie si la méthode obtenir_solde retourne correctement le solde du compte
        """
        compte = CompteBancaire(200)
        self.assertEqual(compte.obtenir_solde(), 200)

if __name__ == '__main__':
    unittest.main()
