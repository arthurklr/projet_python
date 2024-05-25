mot_mystere = 'python'

mot_public = '_' * len(mot_mystere)

vie = 7


while vie > 0 and mot_mystere != mot_public:
    lettre = input("Donnez une lettre : ")
    if lettre in mot_mystere:
        for i in range(len(mot_mystere)):
            if mot_mystere[i] == lettre:
                mot_public = mot_public[:i] + lettre + mot_public[i + 1 :]
    else: 
        vie -= 1
    if mot_public == mot_mystere:
        print("Vous avez gagnez, le mot était", mot_mystere)
    elif vie ==0:
        print("Vous avez perdu")
    else:
        print("Vous avez", vie)
        print("Le mot est :", mot_public)