# Programme d'un jeu du mot mystère

import random

# Liste des mots mystères
liste_mots = ['marissa', 'corentin', 'alain', 'matheo']

# Choisir un mot mystère aléatoirement
mot_mystere = random.choice(liste_mots)

# Initialiser les variables
mot_public = '_' * len(mot_mystere)
vie = len(mot_mystere)
lettre_utilisees = []

# Boucle principale du jeu
while vie > 0 and mot_mystere != mot_public:
    lettre = input("Donnez une lettre : ")
    if len(lettre) !=1:
        print("Veuillez entrer qu'une seule lettre.")
        continue
    if lettre in lettre_utilisees:
        print("Vous avez déjà utilisé cette lettre")
        continue
    lettre_utilisees.append(lettre)
    if lettre in mot_mystere:
        for i in range(len(mot_mystere)):
            if mot_mystere[i] == lettre:
                mot_public = mot_public[:i] + lettre + mot_public[i + 1 :]
    else: 
        vie -= 1
    
    if mot_public == mot_mystere:
        print("Vous avez gagné, le mot était", mot_mystere)
    elif vie == 0:
        print("Vous avez perdu")
    else:
        print("La lettre", lettre, "n'est pas dans le mot.")
        print("Vous avez", vie, "vies restantes.")
        print("Le mot est :", mot_public)
        print("Lettres utilisées : ", lettre_utilisees)