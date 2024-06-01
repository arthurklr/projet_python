# Programme qui vous affiche si vous avez le bac ou non

# Demande à l'utilisateur de saisir sa moyenne et la convertit en nombre à virgule flottante
moyenne = float(input("Quel est votre moyenne ? "))

# Vérifie si la moyenne est dans la plage [10, 12[
if 10 <= moyenne < 12:
    print("Vous avec le bac sans mention")  # Affiche un message indiquant que l'utilisateur a le bac sans mention

# Vérifie si la moyenne est dans la plage [12, 14[
elif 12 <= moyenne < 14:
    print("Vous avez le bac avec mention assez-bien")  # Affiche un message indiquant que l'utilisateur a le bac avec mention assez-bien

# Vérifie si la moyenne est dans la plage [14, 16[
elif 14 <= moyenne < 16:
    print("Vous avez le bac avec mention bien")  # Affiche un message indiquant que l'utilisateur a le bac avec mention bien

# Vérifie si la moyenne est dans la plage [16, 18[
elif 16 <= moyenne < 18:
    print("Vous avez le bac avec mention très bien")  # Affiche un message indiquant que l'utilisateur a le bac avec mention très bien

# Vérifie si la moyenne est dans la plage [18, 20[
elif 18 <= moyenne < 20:
    print("Vous avez le bac avec les félicitations du jury")  # Affiche un message indiquant que l'utilisateur a le bac avec les félicitations du jury

# Si la moyenne n'est pas dans les plages précédentes, vérifie d'autres cas
else:
    # Vérifie si la moyenne est dans la plage [0, 8[
    if 0 <= moyenne < 8:
        print("Vous n'avez pas le bac")  # Affiche un message indiquant que l'utilisateur n'a pas le bac
    
    # Vérifie si la moyenne est dans la plage [8, 10[
    elif 8 <= moyenne < 10:
        print("Vous passez les rattrapages")  # Affiche un message indiquant que l'utilisateur passe les rattrapages
