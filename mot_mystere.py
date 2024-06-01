# Programme d'un jeu du mot mystère

import random

# Liste des mots mystères
liste_mots = ['marissa', 'corentin', 'alain', 'matheo']

# Choisir un mot mystère aléatoirement
mot_mystere = random.choice(liste_mots)

# Initialiser les variables
mot_public = '_' * len(mot_mystere)  # Initialiser le mot public avec des tirets bas pour chaque lettre du mot mystère
vie = len(mot_mystere)  # Nombre de vies initialisé à la longueur du mot mystère
lettre_utilisees = []  # Liste pour stocker les lettres déjà utilisées

# Boucle principale du jeu
while vie > 0 and mot_mystere != mot_public:
    lettre = input("Donnez une lettre : ")  # Demander au joueur de deviner une lettre

    # Vérifier si la saisie est une seule lettre
    if len(lettre) != 1:
        print("Veuillez entrer qu'une seule lettre.")
        continue

    # Vérifier si la lettre a déjà été utilisée
    if lettre in lettre_utilisees:
        print("Vous avez déjà utilisé cette lettre")
        continue

    lettre_utilisees.append(lettre)  # Ajouter la lettre à la liste des lettres utilisées

    # Vérifier si la lettre devinée est dans le mot mystère
    if lettre in mot_mystere:
        # Mettre à jour le mot public pour révéler les occurrences de la lettre devinée
        for i in range(len(mot_mystere)):
            if mot_mystere[i] == lettre:
                mot_public = mot_public[:i] + lettre + mot_public[i + 1 :]
    else:
        vie -= 1  # Décrémenter le nombre de vies si la lettre devinée n'est pas dans le mot mystère
    
    # Afficher le résultat du tour
    if mot_public == mot_mystere:
        print("Vous avez gagné, le mot était", mot_mystere)
    elif vie == 0:
        print("Vous avez perdu")
    else:
        print("La lettre", lettre, "n'est pas dans le mot.")
        print("Vous avez", vie, "vies restantes.")
        print("Le mot est :", mot_public)
        print("Lettres utilisées : ", lettre_utilisees)
