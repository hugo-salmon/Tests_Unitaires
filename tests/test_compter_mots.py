import unittest
from functions import compter_mots

class TestCompterMots(unittest.TestCase):
    """
    Classe de test pour la fonction compter_mots
    """

    def test_phrase_vide(self):
        """
        Vérifie si une phrase vide retourne 0
        """
        self.assertEqual(compter_mots(""), 0)

    def test_un_mot(self):
        """
        Vérifie si une phrase avec un seul mot retourne 1
        """
        self.assertEqual(compter_mots("Test"), 1)

    def test_mots_espaces_en_plus(self):
        """
        Vérifie si une phrase avec des espaces en plus retourne le nombre correct de mots.
        """
        self.assertEqual(compter_mots("   Test du nombre de mots   "), 5)

    def test_phrase_ponctuation(self):
        """
        Vérifie si une phrase avec de la ponctuation retourne le nombre correct de mots
        """
        self.assertEqual(compter_mots("Ceci est un test avec de la ponctuation!"), 8)

    def test_phrase_caracteres_speciaux(self):
        """
        Vérifie si une phrase avec des caractères spéciaux retourne le nombre correct de mots
        """
        self.assertEqual(compter_mots("Test avec des caractères spéciaux : /$%#@!"), 7)

if __name__ == '__main__':
    unittest.main()