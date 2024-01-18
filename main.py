from functions import*


if __name__ == '__main__':

    print()
    print()
    print("MENU PRINCIPALE : \n ")
    print()
    print("Où souhaitez-vous aller ?")
    print(" 1 - Menu lecteur  \n 2 - Bibliothèque \n 3 - Menu de recommandation \n")
    a = 0
    while a < 1 or a > 3:
        a = int(input("Saisissez le numéro correspondant à votre choix: \n"))

    if a == 1:
        print()
        menu_lecteur()
    if a == 2:
        print()
        menu_livres()
    if a == 3:
        print()
        menu_recommandation()















