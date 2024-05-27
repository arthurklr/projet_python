# Programme qui vous affiche si vous avez le bac ou non

moyenne = float(input("Quel est votre moyenne ? "))

if 10 <= moyenne < 12:
    print("Vous avec le bac sans mention")
elif 12 <= moyenne < 14:
    print("Vous avez le bac avec mention assez-bien")
elif 14 <= moyenne < 16:
    print("Vous avez le bac avec mention bien")
elif 16 <= moyenne < 18:
    print("Vous avez le bac avec mention très bien")
elif 18 <= moyenne < 20:
    print("Vous avez le bac avec les félicitations du jury")
else:
    if 0<= moyenne < 8:
        print("Vous n'avez pas le bac")
    elif 8 <= moyenne < 10:
        print("Vous passez les rattrapages")
