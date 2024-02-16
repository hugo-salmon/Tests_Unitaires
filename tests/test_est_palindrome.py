import unittest
from functions import est_palindrome

class TestEstPalindrome(unittest.TestCase):
    """
    Classe de test pour la fonction est_palindrome
    """

    def test_palindrome(self):
        """
        Vérifie si une chaîne de caractères palindrome est détectée correctement
        """
        self.assertTrue(est_palindrome("raDar"))

    def test_palindrome_avec_espaces(self):
        """
        Vérifie si une chaîne de caractères avec des espaces est détectée correctement comme un palindrome
        """
        self.assertTrue(est_palindrome("   Kayak. radar !kayak   "))

    def test_non_palindrome(self):
        """
        Vérifie si une chaîne de caractères qui n'est pas un palindrome est détectée correctement
        """
        self.assertFalse(est_palindrome("test"))

    def test_palindrome_majuscules_minuscules(self):
        """
        Vérifie si la casse des lettres est ignorée lors de la détection des palindromes
        """
        self.assertTrue(est_palindrome("RaDAr"))

if __name__ == '__main__':
    unittest.main()