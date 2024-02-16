import unittest
from functions import Rectangle

class TestRectangle(unittest.TestCase):
    """
    Classe de test pour la classe Rectangle.
    """

    def test_calculer_perimetre(self):
        """
        Vérifie si la méthode calculer_perimetre() calcule correctement le périmètre du rectangle
        """
        rectangle = Rectangle(15, 20)
        self.assertEqual(rectangle.calculer_perimetre(), 70)

    def test_calculer_surface(self):
        """
        Vérifie si la méthode calculer_surface() calcule correctement la surface du rectangle
        """
        rectangle = Rectangle(15, 20)
        self.assertEqual(rectangle.calculer_surface(), 300)

if __name__ == '__main__':
    unittest.main()




