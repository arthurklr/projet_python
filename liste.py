# Programme qui affiche une liste de 0 à n-1 (à définir)

def simple_range(n):
    # Définition d'une fonction simple_range qui prend un argument n
    l = []  # Initialisation d'une liste vide
    i = 0   # Initialisation d'un compteur à 0
    
    while i < n:  # Boucle tant que le compteur est inférieur à n
        l.append(i)  # Ajout de la valeur actuelle du compteur à la liste
        i += 1  # Incrémentation du compteur
    
    return l  # Renvoie la liste complète

print(simple_range(10))  # Appel de la fonction simple_range avec n=10 et affichage du résultat
