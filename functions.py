import string
def est_premier(nombre):
    """
    Vérifie si un nombre est premier
    """
    if nombre < 2:
        return False
    for i in range(2, int(nombre ** 0.5)+1):
        if nombre % i == 0:
            return False
    return True

def compter_mots(phrase):
    """
    Compte le nombre de mots dans une phrase.
    """
    if not phrase:
        return 0   
    mots = phrase.split()
    return len(mots)

class CompteBancaire:
    """
    Cette classe représente un compte bancaire
    """

    def __init__(self, solde_initial: float):
        """
        Initialise un nouveau compte bancaire avec un solde initial.
        """
        self.solde = solde_initial

    def deposer(self, montant: float):
        """
        Dépose un montant sur le compte
        """
        self.solde += montant

    def retirer(self, montant: float):
        """
        Retire un montant du compte
        """
        if self.solde < montant:
            raise ValueError("Solde insuffisant")
        self.solde -= montant

    def obtenir_solde(self) -> float:
        """
        Renvoie le solde actuel du compte
        """
        return self.solde

def somme_liste(liste):
    """
    Calcule la somme des éléments d'une liste.
    """
    somme = 0
    for element in liste:
        somme += element 
    return somme

class Rectangle:
    """
    Cette classe représente un rectangle
    """

    def __init__(self, longueur, largeur):
        """
        Initialise un nouveau rectangle avec une longueur et une largeur données
        """
        self.longueur = longueur
        self.largeur = largeur

    def calculer_perimetre(self):
        """
        Calcule le périmètre du rectangle
        """
        return 2 * (self.longueur + self.largeur)

    def calculer_surface(self):
        """
        Calcule la surface du rectangle
        """
        return self.longueur * self.largeur

def est_palindrome(chaine): 
    """
    Vérifie si une chaîne de caractères est un palindrome.
    """
    chaine = chaine.lower()  # Convertit en minuscules
    chaine = chaine.translate(str.maketrans("", "", string.punctuation))  # Supprime la ponctuation
    chaine = chaine.replace(" ", "")  # Supprime les espaces
    chaine_inverse = chaine[::-1]
    return chaine == chaine_inverse

def calcul_moyenne(liste):
    """
    Calcule la moyenne des nombres dans une liste.
    """
    if not liste:
        raise ValueError("La liste ne peut pas être vide.")
    return sum(liste) / len(liste)