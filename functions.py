import time
from math import*

#~~~~~~~~~~~~ PARTIE I ~~~~~~~~~~~~~~~~


#On réalise la fonction ajouter pour ajouter un utilisateur
def ajout():
    print()
    use=str()
    with open("readers.txt","r") as r,  open("pseudo.txt","r") as p, open("booksread.txt","r") as b:
        #On demande à l'utilisateur d'entrer son pseudonyme s'il n'existe pas
        pseudos=p.readline()
        print('Quel est votre pseudonyme ? \n')
        pseudo = str(input())

        while pseudos != "":
            if pseudos == pseudo+'\n':
                pseudo = str(input("Ce pseudonyme est déjà utilisé ! Choisissez-en un autre : \n "))

            pseudos=p.readline()

        use+=pseudo #On ajoute le pseudo dans 'Use' qui sera le mot ajouter dans le fichier readers
        use+=','

        #On demande à l'utilisateur d 'entrer son genre
        i = 0
        g = str()
        while 1 > i or i > 3:
            i = int(input("Quel est votre genre ? \n 1.Homme \n 2.Femme \n 3.Dinosaure \n \n Saisissez le numéro correspondant à votre choix: \n"))

            if i == 1:
                g = '1'
            elif i == 2:
                g = '2'
            elif i == 3:
                g = '3'
        use+=g #On ajoute le numéro correspondant au genre à 'Use'
        use+=','

        #On demande à l'utilisateur d'entrer sa tranche d'âge
        j = 0
        a = str()
        while 1 > j or j > 3:
            j = int(input("Quel est votre âge ? \n 1. <18 ans  \n 2. Entre 18 et 25 ans  \n 3. >25 ans  \n \n Saisissez le numéro correspondant à votre choix: \n"))

            if j == 1:
                a = '1'
            elif j == 2:
                a = '2'
            elif j == 3:
                a = '3'

        use+=a #On ajoute le numéro correspondant à la tranche d'âge à 'Use'
        use+=','

        #On demande à l'utilisateur son types de lectures
        S=str()
        k=0
        while k<1 or k>7:
            k=int(input( 'Quels sont vos styles de lectures ? \n 1. Science-fiction \n 2. Biographie \n 3. Horreur \n 4. Romance \n 5. Fable \n 6. Histoire \n 7. Comédie \n \n Saisissez le numéro correspondant à votre choix: \n'))

            if k == 1:
                S = '1'
            elif k == 2:
                S = '2'
            elif k == 3:
                S = '3'
            elif k == 4:
                S = '4'
            elif k == 5:
                S = '5'
            elif k == 6:
                S = '6'
            elif k == 7:
                S = '7'

        use+=S #On ajoute son style de lecture à 'Use'


        B=books_read() #On importe la fonction books_read qui permet de former une liste des livres lus
        text=str()
        for i in B: #On transforme cette liste en une chaine de caractère
            text+=','
            text+=str(i)


    with open("pseudo.txt","a") as p, open("readers.txt","a") as r, open("booksread.txt","a") as b:
        r.write(use+'\n')
        b.write(pseudo+text+'\n')
        p.write(pseudo+'\n')

    time.sleep(2)
    print("l'utilisateur", pseudo, "a été ajouté.")  # On previent l'utilisateur qu'il à été enregistrer
    print()
    print()
    matrice_lect_ajout()


def note():
    with open("pseudo.txt",'r') as p:
        pseudo=p.readlines()
        u=0
        for i in pseudo:
            u+=1

    z=0
    while z<1 or z>2:
        z=int(input("Souhaitez-vous noter les livres que vous avez lu ? \n 1 - OUI \n 2 - NON \n Saisissez le numéro correspondant à votre choix : \n"))

        if z==1:
            noter_livre(u)
        else:
            menu_lecteur()


#~~~Dictionnaires~~~


#On réalise une fonction qui transforme nos fichiers les infos des fichiers pseudo et readers en liste
def dico_user():
    M = []
    with open('readers.txt', "r") as o, open('pseudo.txt','r') as p:
        user = o.readlines()
        for i in user:
            liste=i.split(',')
            for j in range(len(liste)):
                liste[j] = liste[j].rstrip()

            M.append(liste) #On ajoute cette liste dans une matrice où chaque ligne représente les données de chaque utilisateur

        k=0
        dico={}
        for j in M:
            k+=1
            dico[k]=j #On réalise un dictionaire où les valeurs sont les listes des infos des utilisateurs

        return(dico)

def dico_bookread(): #On réalise un dictionnaire où les valeurs sont les livres lu par l'utilisateur
    M = []
    with open('booksread.txt', 'r') as b, open('pseudo.txt', 'r') as p:
        livreslu = b.readlines() #On créé une liste à partir du fichier booksread
        for i in livreslu:
            liste = i.split(',')  #On défini un élément de la liste à chaque virgule qu'on rentre dans une liste
            for j in range(len(liste)):
                liste[j] = liste[j].rstrip() #On retire les \n

            M.append(liste) #On ajoute notre liste à une matrice

        k = 0
        dico = {}
        for i in M: #On définie un dictionnaire avec commes valeurs les listes de notre matrice
            k += 1
            dico[k] = i

        return (dico)


#On réalise un dictionnaire avec les livres du dépot
def dico_books():
    M = []
    with open('books.txt', "r") as b:
        livres = b.readlines()
        dico={}
        k=0
        for i in livres: #Pour chaque livre on donne une clé k allant de 1 au nombre de livres
            titre = i
            titre = titre.rstrip()

            k+=1
            dico[k]=titre

        return(dico)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#On réalise la fonction pour afficher un utilisateur
def afficher():
    D=dico_user()
    B=dico_books()
    L=dico_bookread()
    a=0
    age=str()
    genre=str()
    style=str()
    with open("readers.txt",'r') as r, open("pseudo.txt","r") as p, open('booksread.txt','r') as b:
        pseud=p.readlines()
        while a<1 or a>len(pseud): #On demande à l'utilisateur quel profil il souhaite afficher
            print('Quel utilisateur voulez-vous afficher ? \n')
            j=1
            for i in pseud:
                print(j,'-',i,'\n') #On affiche les pseudo des profils
                j+=1
            print()
            a=int(input('Saisissez la chiffre correspondant à votre choix: \n'))
            U=D[int(a)]   #On rentre la valeur du dico dans une liste

        #Pour chaque éléments de la liste on associe un statut
        for i in U:                #Pour le genre
            if U[1]=='1':
                genre='Homme'
            elif U[1]=='2':
                genre='Femme'
            elif U[1]=='3':
                genre='Dinosaure'

            if U[2]=='1':                 #Pour l'age
                age='moins de 18 ans'
            elif U[2]=='2':
                age='entre 18 et 25 ans'
            elif U[2]=='3':
                age='plus de 25 ans'

            if U[3]=='1':              #Pour le style de livre
                style='Science-fiction'
            elif U[3]=='2':
                style='Biographie'
            elif U[3]=='3':
                style='Horreur'
            elif U[3]=='4':
                style='Romance'
            elif U[3]=='5':
                style='Fable'
            elif U[3]=='6':
                style='Histoire'
            elif U[3]=='7':
                style='Comédie'

        E = L[int(a)]              #On ouvre le dictionnaire des livres lu
        texte = str()                #On créé un texte des livres lu par le profil
        for i in range(1,len(E)):
            u = E[i]                 #On associe le numéro du livre lu à u
            texte += B[int(u)]+'\n'       #On ouvre le dicotionnaire de livres et on ajoute le livre associé de valeur u

    nom = pseud[a - 1]

    print(
        '  - pseudo: {0} \n  - genre: {1} \n \n  - âge: {2} \n \n  - style de lecture: {3} \n \n  - Livre(s) lu(s): \n \n{4}'.format(nom, genre, age, style, texte))  # On affiche le lecteur



#On réalise la fonction books_read
def books_read():
    D=dico_books()
    with open("books.txt","r") as b, open("pseudo.txt",'r') as p:

        user=p.readlines()
        u=0
        for i in user:
            if i!="":
                u+=1


        print("Lequel de ces livres avez vous déja lu ? \n") #On demande à l'utilisateur les livres qu'il a lu
        livre=b.readlines()
        j=0
        a=0
        cpt=0
        L=[]
        texte=str()
        for i in livre: #La variable i prend la valeur de chaque livre dans le dépot
            j+=1
            print(j,'-',i) #On affiche chaque livre associé à un chiffre
        print()
        print(0 ,'- Validez la saisie \n') #On propose un bouton pour valider la saisie
        print()
        print("Saisissez le numéro des livres lus puis taper 0 pour sauvegarder: \n")
        while a> -1 and a<=j:
            a = int(input())  
            if a>0: #Si le numéro est valide, on renvoie le titre du livre, le nombre livre selectionnés
                b=int(a)
                texte+= D[b]+'\n '
                cpt+=1
                print()
                print(D[b])
                print(cpt,'livre(s) sélectionné(s) \n')
                L.append(a)        #On ajoute le numéro du livre à une liste
                print('Sélectionnez un autre livre ou sauvegarder avec 0')

            else:

                print('Vous avez lu',cpt,'livres :\n',texte) #Si la saisie est validé on return la liste de livres lu
                return(L)





#On réalise une fonction qui permet de supprimer un lecteur
def suppr():
    D=dico_user()
    a=0
    with open("readers.txt",'r') as r, open("pseudo.txt","r") as p:
        pseud=p.readlines()
        while a<1 or a>len(pseud): #On demande à l'utilisateur quel profil il souhaite supprimer
            print('Quel utilisateur voulez-vous supprimer ? \n')
            j=1
            for i in pseud:
                print(j,'-',i,'\n') #On affiche tous les pseudos
                j+=1
            a=int(input("Saisissez le numéros de l'utilisateur à supprimer: \n"))

        nom=pseud[a-1]

        verif=0
        while verif<1 or verif>2: #On demande à l'utlisateur s'il est sûr de son choix
            print('Etes vous sûr de vouloir supprimer le profil de {}'.format(nom))
            print(' 1-OUI \n 2-NON')
            verif=int(input( 'Saisissez 1 ou 2: \n'))

            if verif==2: #Si il tape NON on le renvoie au menu prinicipale
                #retourner le menu
                print()
            elif verif==1:      #Si il tape OUI on renvoie la fonction suppression de a( le numéro du profil à supprimer)
                s=supression_profil(a)
                print('Le profil à été supprimer')



#On définit la fonction supression
def supression_profil(a):
    #On réecrit tous le contenu des fichiers (ouverts en read) où des éléments sont à supprimer
    #On commence par le fichier booksread.txt
    with open('pseudo.txt', 'r') as pp, open('readers.txt', 'r') as r, open('booksread.txt','r') as b:
        L = []
        lignes = b.readlines()
        k=0  #On défini k une variable qui sert uniquemnt à être comparé avec a
        for i in lignes:
            k+=1
            if a!=k:  #Si k et a (numéro associer à l'utilisateur à supprimer) diffère on ajoute la ligne(i) du fichier à notre liste
                L.append(i)
        text = str()
        for j in range(len(L)): #On transforme notre liste en texte
            text+=L[j]

        #On reproduit la même chose avec le fichier readers.txt
        M = []
        u = 0
        for i in r:
            u += 1
            if a != u:
                M.append(i)
        text1 = str()
        for j in range(len(M)):
            text1 += M[j]

        #On reproduit la même chose avec le fichier pseudo
        N = []
        v = 0
        for i in pp:
            v += 1
            if a != v:
                N.append(i)
        text2 = str()
        for j in range(len(N)):
            text2 += N[j]

    #On réecrit nos fichiers (ouverts en write) avec nos 3 textes
    with open('pseudo.txt','w') as p, open('readers.txt','w') as r, open('booksread.txt','w') as b:
        p.write(text2)
        r.write(text1)
        b.write(text)

    matrice_supp_lecteur(a-1)




#Exactement la même fonction que afficher avec comme seul changement le "modifier" (ligne 319)
def afficher_for_supp():
    D = dico_user()
    B = dico_books()
    L = dico_bookread()
    a = 0
    age = str()
    genre = str()
    style = str()
    with open("readers.txt", 'r') as r, open("pseudo.txt", "r") as p, open('booksread.txt', 'r') as b:
        pseud = p.readlines()
        while a < 1 or a > len(pseud):  # On demande à l'utilisateur quel profil il souhaite afficher
            print('Quel utilisateur voulez-vous modifier ? \n')
            j = 1
            for i in pseud:
                print(j, '-', i, '\n')  # On affiche les pseudo des profils
                j += 1
            a = int(input("Saisissez le numéro de l'utilisateur à modifer : \n"))
            U = D[int(a)]  # On rentre la valeur du dico dans une liste

        # Pour chaque éléments de la liste on associe un statut
        for i in U:
            if U[1] == '1':
                genre = 'Homme'
            elif U[1] == '2':
                genre = 'Femme'
            elif U[1] == '3':
                genre = 'Dinosaure'

            if U[2] == '1':
                age = 'moins de 18 ans'
            elif U[2] == '2':
                age = 'entre 18 et 25 ans'
            elif U[2] == '3':
                age = 'plus de 25 ans'

            if U[3] == '1':
                style = 'Science-fiction'
            elif U[3] == '2':
                style = 'Biographie'
            elif U[3] == '3':
                style = 'Horreur'
            elif U[3] == '4':
                style = 'Romance'
            elif U[3] == '5':
                style = 'Fable'
            elif U[3] == '6':
                style = 'Histoire'
            elif U[3] == '7':
                style = 'Comédie'

        E = L[int(a)]  # On ouvre le dictionnaire des livres lu
        texte = str()  # On créé un texte des livres lu par le profil
        for i in range(1, len(E)):
            u = E[i]  # On associe le numéro du livre lu à u
            texte += B[int(u)]+'\n '  # On ouvre le dicotionnaire de livres et on ajoute le livre associé de valeur u

    nom = pseud[a - 1]

    print('  - pseudo: {0} \n  - genre: {1} \n \n  - âge: {2} \n \n  - style de lecture: {3} \n \n  - Livre(s) lu(s): \n \n {4}'.format(nom, genre, age, style, texte))  # On affiche le lecteur

    return(a)

def modif():
    A=afficher_for_supp() #On affiche les données du lecteur à modifier
    print()
    print()
    a=0
    while a<1 or a>5:  #L'utilisateur choisi la donné à modifier
        print('Quel éléments voulez-vous modifier ? \n 1 - Pseudo \n 2 - Age \n 3 - Genre \n 4 - Style de lecture \n 5 - Livre(s) lu(s) \n')
        a=int(input("Saisissez le numéro correspondant à votre choix :\n"))
        if a==1:                        #Pour chaque données à modifier on associe une fonction
            m=modif_pseudo(A)
        elif a==2:
            m=modif_age(A)
        elif a==3:
            m=modif_genre(A)
        elif a==4:
            m=modif_styles(A)
        elif a==5:
            m=modif_livreslu(A)

#On réalise la fonction pour modifier le pseudo
def modif_pseudo(a):
    D=dico_user()
    B=dico_bookread()
    with open('pseudo.txt','r')as p, open('readers.txt','r') as r, open('booksread.txt','r') as b:
       pseudo=p.readlines()
       user=r.readlines()
       books=b.readlines()
       k=0
       L=[]
       text=str()
       for i in pseudo:   #Pour chaque pseudo dans le fichier pseudo on compare k (valeur qui prend +1 à chaque lecteur du fichiers) et a (valeur associer à l'utilisateur )
           k+=1
           if k==a:
               pseudo=str(input('Entrez un nouveau pseudonyme :\n')) #Si k==a on réecrit le pronom dans notre texte
               text+=pseudo+'\n'
           else:
               text+=i      #Sinon on recopie les pseudos deja presents



       L = D[a]   #L notre liste qui prend la liste associée à notre lecteur grace au dictionnaire dico_user
       chiffre=str()
       text2=str()

       for i in range(1,len(L)):  #Avec les valeurs de i à partir de 1 qui représentent les genre,age,styles des lecteur on écrit chiffre
           chiffre+=','+L[i]

       text2+=pseudo+chiffre #On ecrit un deuxième texte avec notre nouveau pseudo et nos chiffres


#On réalise la même chose avec les données des livres lu
       M=B[a]
       chiffre2 = str()
       for i in range(1,len(M)):
            chiffre2+=','+M[i]

       text3 = pseudo+chiffre2



#On réecrit nos fichiers ouverts en write avec nos 3 textes
    with open ('pseudo.txt','w') as p, open('readers.txt','w') as r, open('booksread.txt','w') as b:
        r.write(text2)
        p.write(text)
        b.write(text3)

    print()
    print('Votre nouveau pseudonyme est :', pseudo)


#On réalise la fonction pour modifier l'age du lecteur
def modif_age(a):
    with open('readers.txt','r') as r , open('pseudo.txt','r') as p:
        pseudo=p.readlines()
        user=r.readlines()
        R=dico_user()
        L=R[a]      #On ouvre la liste correspondant au infornations du lecteur dans le fichiers readers.txt
        j = 0
        v = str()
        texte=str()
        while 1 > j or j > 3:   #On demande à l'utilisateur de ressaisir son âge
            j = int(input("Quel est votre âge ? \n 1. <18 ans  \n 2. Entre 18 et 25 ans  \n 3. >25 ans  \n Saisissez le numéro correspondant à votre choix : \n"))
            if j == 1:
                v = '1'
            elif j == 2:
                v = '2'
            elif j == 3:
                v = '3'


        L[2]=v       #On donne la nouvelle valeur de l'âge à notre liste
        liste=str()
        for i in range(1,len(L)):
            liste+=','+L[i]      #On transforme la liste en une chaine de caractère
        texte+=L[0]+liste

        TEXT=str()
        k=0
        for i in user:
            k+=1
            if k==a:
                TEXT+=texte+'\n'  #On recopie entièrement notre fichier
            else:
                TEXT+=i



    with open('readers.txt','w') as r:  #On réecrit entierement notre fichier
        r.write(TEXT)


    print("L'âge de votre utilisateur à été modifier")

#On réalise la fonction pour modifier le genre du lecteur
def modif_genre(a):
    with open('readers.txt', 'r') as r, open('pseudo.txt','r') as p:
        pseudo=p.readlines()
        user = r.readlines()
        R = dico_user()
        L = R[a]
        texte = str()
        i = 0
        g = str()
        while 1 > i or i > 3:  #On demande à l'utilisateur de saisir son nouveau genre
            i = int(input("Quel est votre genre ? \n 1.Homme \n 2.Femme \n 3.Dinosaure \n Saisissez le numéro correspondant à votre choix: \n"))
            if i == 1:
                g = '1'
                sexe='Homme'
            elif i == 2:
                g = '2'
                sexe='Femme'
            elif i == 3:
                g = '3'
                sexe='Dinosaure'


        L[1] = g   #On remplace l'ancien âge pour sa nouvelle valeur
        liste = str()
        for i in range(1,len(L)):
            liste+=','+L[i]
        text=L[0]+liste  #On transforme notre liste en str


        k = 0
        for i in user:
            k += 1
            if a == k:              #On recopie notre texte
                texte+=text+'\n'
            else:
                texte+=i


    with open('readers.txt', 'w') as r:   #On réecrit entièrement notre fichier
        r.write(texte)

    print("L'utilisateur est désormais un(e)",sexe )


#On réalise la fonction pour modifier le style de livre du lecteur
def modif_styles(a):
    with open('readers.txt', 'r') as r, open('pseudo.txt','r') as p:
        user = r.readlines()
        R = dico_user()
        L = R[a]
        texte = str()

        S = str()
        k = 0
        while k < 1 or k > 7:   #On demande à l'utilisateur de saisir à nouveau son style de lecteur
            k = int(input(
                'Quels sont vos styles de lectures ? \n 1. Science-fiction \n 2. Biographie \n 3. Horreur \n 4. Romance \n 5. Fable \n 6. Histoire \n 7. Comédie \n Saisissez le numéro correspondant à votre choix: \n'))
            if k == 1:
                S = '1'
                style='Science-fiction'
            elif k == 2:
                S = '2'
                style='Biographie'
            elif k == 3:
                S = '3'
                style='Horreur'
            elif k == 4:
                S = '4'
                style='Romance'
            elif k == 5:
                S = '5'
                style='Fable'
            elif k == 6:
                S = '6'
                style='Histoire'
            elif k == 7:
                S = '7'
                style='Comédie \n'


        L[3] = S          #On remplace le numéro de style de lecture par sa nouvelle valeur
        liste = L[0]
        for i in range(1,len(L)):
            liste+= ','+L[i]

        k = 0
        for i in user:
            k += 1                     #On copie notre fichier avec les nouvelles informations
            if a == k:
                texte+=liste+'\n'
            else:
                texte+=i


    with open('readers.txt', 'w') as r:    #On réecrit entièrement notre fichier
        r.write(texte)

    print('Votre style de lecture est définie sur:',style )


def modif_livreslu(a):
    with open('books.txt','r') as b:
        B=dico_books()
        livres=b.readlines()
        for i in range(len(livres)):
            livres[i]=livres[i].rstrip()

        R=dico_bookread()
        E = R[int(a)]
        print(E[0],' a lu :')

        texte = str()
        k=0
        for i in range(1, len(E)):
            u = E[i]
            k+=1
            q=str(k)               # On associe le numéro du livre lu à u
            texte += q+' - '+B[int(u)]+'\n'
        print(texte)
        z=0
        while z<1 or z>3 :
            print('Que souhaitez vous faire ? \n 1 - Ajouter un livre \n 2 - Supprimer un livre \n 3 - Noter mes livres \n Saisissez le numéro correpondant à votre choix: \n ')
            z=int(input())
            if z==1:
                ajout_livres_lu_off(a)
                print("Les livres ont bien été ajouté ")
                modif()
            elif z==2:
                print()
            elif z == 3:
                noter_livre(a)

def ajout_livre_lu(a):
    with open("books.txt",'r') as b, open("booksread.txt",'r') as br:
        B=dico_books()
        R=dico_bookread()
        E=R[a]
        livres_lu = []
        livres = []
        for i in B.values():
            livres.append(i)

        for i in range(1,len(E)):
            u = E[i]
            v = int(u)
            livres_lu.append(B[v])

        for i in livres_lu:
            if i in livres:
                ind = livres.index(i)
                del livres[ind]

        texte=str()
        for i in livres_lu:
            texte+=i+'\n '

        k=0
        cpt=len(livres_lu)
        cpt2=0

        for i in livres:
            k+=1
            print(k,'-',i)
            print()
        print('Lesquels de ses livres voulez-vous ajoutez à votre liste de lecture ? \n')
        print("Saisissez le numéro des livres à ajouter puis saisissez 0 pour valider: \n")
        z=0
        while z>-1 and z<=k:
            z = int(input())
            if z>0:
                b = int(z)
                texte += livres[b-1]+'\n '
                cpt2 += 1
                cpt += 1
                print()
                print(livres[b-1])
                print(cpt2, 'livre(s) sélectionné(s) \n')
                livres_lu.append(livres[b-1])  # On ajoute le numéro du livre à une liste
                print('Sélectionnez un autre livre ou sauvegarder avec 0')

            else:
                print('Vous avez lu', cpt, 'livres :\n',texte)

                return(livres_lu)


def ajout_livres_lu_off(a):
    with open('books.txt','r') as b, open('booksread.txt','r') as br:
        R=dico_user()
        E=R[a]
        texte = E[0]
        copie=str()
        livres = b.readlines()
        nouveau_livres_lu=[]
        for i in range(len(livres)):
            livres[i] = livres[i].rstrip()

        livre_lu = ajout_livre_lu(a)

        for i in livre_lu:
            if i in livres:
                ind = livres.index(i)
                ind += 1
                nouveau_livres_lu.append(ind)

        for i in nouveau_livres_lu:
            x = str(i)
            texte += ',' + x
        texte += '\n'

        L=br.readlines()
        for i in range(len(L)):
            if i == a-1:
                copie+=texte
            else:
                copie+=L[i]


    with open('booksread.txt','w') as r:
        r.write(copie)

def suppr_livre_lu(a):
    with open("books.txt", 'r') as b, open("booksread.txt", 'r') as br:
        B = dico_books()
        R = dico_bookread()
        E = R[a]
        k = 0
        for i in range(1, len(E)):
            c = int(E[i])
            k += 1
            print(k, ' - ', B[c])
        print()
        print()
        print('Lesquels de ses livres voulez-vous supprimer de votre liste de lecture ? \n')

        z = 0
        while z < 1 or z > k:
            z = int(input("Saisissez le numéro du livre à supprimer: \n"))


        del E[z]
        copie = str()
        livres_lu = br.readlines()
        texte = ','.join(E)
        texte = texte + '\n'
        for i in range(len(livres_lu)):
            if a - 1 == i:
                copie += texte
            else:
                copie += livres_lu[i]

    with open("booksread.txt", 'w') as m:
        m.write(copie)


# ~~~~~~~~~~ PARTIE II ~~~~~~~~~~~~

#On réalise la fonction pour afficher les livres de la bibliotheque
def aff_livre():
    B=dico_books()
    print("Voici les livres présents dans la bibliothèque : \n")
    for i in B.values():                                             #On affiche les valeurs du dictionnaire contennant les livres
        print(i)



def ajout_livre():
    #ajout d'un livre par l'utilisateur
    B=dico_books()
    a=0
    cpt=0

    with open("books.txt","a") as l:
        p=str(input("Ajoutez le titre du livre souhaité: \n",))       #On demande le titre du livre à ajouter

        for i in B.values():  #On verifie si le livre n'est pas déja présent dans la bibliotheque
            if p==i:
                cpt+=1

        if cpt==0:
            l.write(p+'\n')                        #Si le livre n'existe pas on rajoute le nouveau titre
            print(p,'a été ajouté à la bibliothèque \n ')
            matrice_livre_ajout()
        else:
            print("Ce livre est déjà présent dans la bibliothèque ! \n ")#Sinon prévenir que le livre existe déja



def modif_livre():
    #modification d'un livre de la liste
    B=dico_books()
    k=0
    copy=str()
    for i in B.values():                #On affiche tous les livres présents dans la bibliotheque
        k+=1
        print(k,'-', i)
    print()
    z = 0
    while z<1 or z>k:
        print("Quel livre souhaitez-vous modifier ? \n")
        z=int(input('Saisissez le numéro du livre à modifer: \n'))        #On demande de saisir le numéro du livre à modifier

        modif = B[z]
        livre = input('Entrez le nouveau nom du livre: \n')            #On demande de saisir le nouveau titre du livre

        cpt=0
        for i in B.values():
            if i==livre:   #On vérifie si il n'est pas déja présent dans la bibliotheque
                cpt+=1

        if cpt==0:
            B[z]=livre        #On ajoute notre livre au dictionnaire
        else:
            print("Ce titre est déjà présent dans la bibliothèque") #Sinon on prévient que le livre est déja existant
            time.sleep(3)
            menu_livres()
    for i in B.values():                        #On recopie un texte avec les nouvelles valeurs du dico
        copy+=i+'\n'

    with open('books.txt','w') as b:                   #On réecrit notre bibliotheque
        b.write(copy)
    print('Le livre',modif,'a été modifier en',B[z])


#On réalise la fonction pour supprimer un livre
def suppr_livre():
    with open('booksread.txt','r') as r, open('books.txt', 'r') as b: #On ouvre nos fichiers en mode READ
        B=dico_books()    #J 'ouvre le dictionnaire des livres
        R=dico_bookread    #j'ouvre le dico des livres lus
        k=0
        copy=str()
        copy4=str()
        ligne=r.readline()   #On ouvre le fichiers booksread en mode READLINE une première fois
        for i in B.values():    #On affiche tous les livres de la bibliotheque sous format 1 - Titre
            k += 1               #k prend des valeurs de 1 au nombre de livre
            print(k, '-', i)
        print()
        z=0
        # On demande à l'utilisateur le livre à supprimer
        while z<1 or z>k:                                       #On effectue une saisie sécurisé, z doit être inférieur à k
            print("Quel livre voulez-vous supprimer ? \n")
            z=int(input("Saisissez le numéro correspondant au livre que vous souhaitez supprimer: \n"))

        # z sera le numéro associé à la clé de notre livre
        print("Etes-vous sûr de vouloir supprimer",B[z] )         #On demande une confirmation à l'utilisateur
        verif=0
        while verif<1 or verif>2:
            verif=int(input(' 1 - OUI \n 2 - NON \n Saisissez 1 pour confirmer la suppression ou 2 pour annuler: \n'))

        if verif==1:    # Si l'utilisateur confirme
            del B[z]   #On supprimer d'abord le livre du dico grâce à sa clé

            for i in B.values():  #On recopie les nouvelles valeurs du dictionnaires
                copy += i+'\n'

            # puis on le supprime dans book_read
            while ligne!="":   #on veut parcourir le fichier qu'on a ouvert en readline plus tôt tant que le texte n'est pas vide
                liste = ligne.split(',')  #On change notre chaine de caractère en liste
                for j in range(len(liste)):
                    liste[j] = liste[j].rstrip()  #pour chaque éléments de la liste en retire les \n avec rstrip

                copy2=[]  #On initialise une liste
                for k in liste: #Pour chaque éléments k de la liste:
                    if k!=str(z):         #On la compare avec notre z
                        copy2.append(k)    #si z et k diffèrent on les ajoute à notre liste, on se retrouve avec une liste sans z
                    copy3=','.join(copy2)+'\n'   #on change notre liste en chaine de caractère recopiant toute notre ligne sauf le chiifre z

                ligne=r.readline()    #On refait un readline pour changer de ligne jusqu'à ce qu'elle soit vide
                copy4 += copy3  #on ajoute à un texte les nouvelles lignes du fichiers

        elif verif == 2: #Si l'utilisateur confirme pas on le renvoie au menu
            menu_livres()


    with open("books.txt", 'w') as b, open("booksread.txt",'w') as r: #On ouvre nos fichiers en mode WRITE
        b.write(copy)           #On recopie nos deux textes dans leurs fichiers respectifs
        r.write(copy4)
        print('Le livre à bien été supprimer de la bibliothèque')   #On renvoie un message à l'utilisateur

    matrice_livre_supp(z-1)

#~~~~~~~~~ MENUS ~~~~~~~~

def MENU_PRINCIPALE():
    print()
    print()
    print("MENU PRINCIPALE : \n ")
    print()
    print("Où souhaitez-vous aller ?")
    print(" 1 - Menu lecteur  \n 2 - Bibliothèque \n 3 - Menu de recommandation \n")
    a=0
    while a<1 or a>3:
        a=int(input("Saisissez le numéro correspondant à votre choix: \n"))

    if a==1:
        print()
        menu_lecteur()
    if a==2:
        print()
        menu_livres()
    if a==3:
        menu_recommandation()



def menu_lecteur():
    print()
    print("MENU LECTEUR : \n")
    print()
    print("Que souhaitez-vous faire ? \n")
    print(" 1 - Ajouter un lecteur \n 2 - Afficher le profil d'un lecteur \n 3 - Modifier un lecteur \n 4 - Supprimer un lecteur \n 5 - Retour au menu principale \n")
    a=0
    while a<1 or a>5:
        a=int(input("Saisissez le numéro correspondant à votre choix : \n"))

    if a==1:
        ajout()
        time.sleep(3)
        note()
    elif a==2:
        afficher()
    elif a==3:
        modif()
    elif a==4:
        suppr()
    elif a==5:
        MENU_PRINCIPALE()

    time.sleep(6)
    menu_lecteur()

def menu_livres():
    print()
    print("BIBLIOTHEQUE: \n")
    print()
    print("Que souhaitez-vous faire ? \n")
    print(" 1 - Visiter la bibliotheque \n 2 - Ajouter un livre à la bibliotheque \n 3 - Modifier le titre d'un livre de la bibliotheque \n 4 - Supprimer un livre de la bibliotheque \n 5 - Retourner au menu principale \n ")
    a=0
    while a<1 or a>5:
        a=int(input("Saisir le numéro correspondant à votre choix: \n"))

    if a==1:
        aff_livre()
    elif a==2:
        ajout_livre()
    elif a==3:
        modif_livre()
    elif a==4:
        suppr_livre()
    elif a==5:
        MENU_PRINCIPALE()

    time.sleep(3)
    menu_livres()


def menu_recommandation():

    p=open("pseudo.txt",'r')
    print("MENU RECOMMANDATION:")
    print()
    print()
    pseudos = p.readlines()
    nom = str(input("Saisissez votre pseudo :"))
    while nom+'\n' not in pseudos:
        nom =str(input("Saisissez votre pseudo:"))
    p.close()
    p=open("pseudo.txt",'r')
    pseudo=p.readline()
    cpt=1
    while pseudo != nom+'\n':
        cpt+=1
        pseudo=p.readline()

    recommandation(cpt)

    MENU_PRINCIPALE()


#~~~~~~~~~~ MATRICE ~~~~~~~~~~~~

def matrice():
    with open("booksread.txt",'r') as r, open("books.txt",'r') as b, open("pseudo.txt",'r') as p, open('matrice.txt','w') as m:
        M=[]
        B=dico_books()
        nbboks=len(B)
        U=dico_user()
        nbuser=len(U)
        texte=str()
        for i in range(1,nbuser+1):
            L=[]
            for j in range(1,nbboks+1):
                val=str(0)
                L.append(val)
            M.append(L)


        for i in M:
            l=i
            joindre=' '.join(l)
            texte+=joindre+'\n'

        m.write(texte)
    return(M)


def matrice_supp_lecteur(a):
    with open("booksread.txt", 'r') as r, open("books.txt", 'r') as b, open("pseudo.txt", 'r') as p, open('matrice.txt','r') as m:

        M=[]
        texte2=str()
        matrice=m.readlines()

        for i in matrice:
            L= i.split(' ')
            for j in range(len(L)):
                L[j]=L[j].rstrip()
            M.append(L)


        del M[a]

        for i in M:
            texte=str()
            for j in i:
                texte+=str(j)+' '
            texte2+=texte+'\n'



    with open('matrice.txt','w') as m:
        m.write(texte2)

def matrice_lect_ajout():
    with open("booksread.txt", 'r') as r, open("books.txt", 'r') as b, open("pseudo.txt", 'r') as p, open('matrice.txt','r') as m:

        M=[]
        texte2=str()
        matrice=m.readlines()

        for i in matrice:
            L= i.split(' ')
            for j in range(len(L)):
                L[j]=L[j].rstrip()
            M.append(L)

        liste=[]

        books=b.readlines()
        for i in books:
            liste.append(0)


        M.append(liste)

        for i in M:
            texte=str()
            for j in i:
                texte+=str(j)+' '
            texte2+=texte+'\n'



    with open('matrice.txt','w') as m:
        m.write(texte2)




def matrice_livre_ajout():
    with open("booksread.txt", 'r') as r, open("books.txt", 'r') as b, open("pseudo.txt", 'r') as p, open('matrice.txt','r') as m:

        M=[]
        texte2=str()
        matrice=m.readlines()

        for i in matrice:
            u=i+" 0"
            L= u.split(' ')
            for j in range(len(L)):
                L[j]=L[j].rstrip()
            M.append(L)


        for i in range(len(M)):
            print(i)
            for j in range(len(M[i])):
                print(j)
                if M[i][j] == '':
                    del M[i][j]


        for i in M:
            texte=str()
            for j in i:
                texte+=str(j)+' '
            texte2+=texte+'\n'



    with open('matrice.txt','w') as m:
        m.write(texte2)


def matrice_livre_supp(z):
    with open("booksread.txt", 'r') as r, open("books.txt", 'r') as b, open("pseudo.txt", 'r') as p, open('matrice.txt','r') as m:

        M = []
        texte2 = str()
        matrice = m.readlines()

        for i in matrice:
            L = i.split(' ')
            for j in range(len(L)):
                L[j] = L[j].rstrip()
            M.append(L)



        for i in range(len(M)):
            del M[i][z]

        for i in M:
            texte = str()
            for j in i:
                texte += str(j) + ' '
            texte2 += texte + '\n'



    with open('matrice.txt','w') as m:
        m.write(texte2)


#~~~~~~~~~ PARTIE III ~~~~~~~~~~~~~~~~

def noter_livre(a):
    with open("booksread.txt", 'r') as r, open("books.txt", 'r') as b, open("pseudo.txt", 'r') as p, open('matrice.txt','r') as m:

        B=dico_books()
        nbboks=len(B)
        M=[]
        R=dico_bookread()
        L=R[int(a)]
        texte2=str()
        print(L[0],',')
        print()

        lignes=m.readline()
        while lignes!="":
            liste = lignes.split(' ')
            for j in range(len(liste)):
                liste[j]=liste[j].rstrip()
            M.append(liste)
            lignes=m.readline()


        for i in range(1,len(L)):
            x=L[i]
            for j in range(nbboks+1):
                y=str(j)
                if x==y:
                     M[a-1][j-1] = 0
                     while M[a-1][j-1]<1 or M[a-1][j-1]>5:
                        print('Vous avez lu ce livre',B[j],': \n')
                        M[a-1][j-1]=int(input('Notez le livre sur 5: \n'))


        for i in M:
            texte=str()
            for j in i:
                texte+=str(j)+' '
            texte2+=texte+'\n'

        print()
        print()
        print("Vos notes ont bien été enregistrée !")

    with open("matrice.txt",'w') as m:
        m.write(texte2)


def similarite():
    with open("matrice.txt", 'r') as m:
        M = []
        ligne = m.readline()
        while ligne != "":
            L = ligne.split(" ")
            for i in range(len(L)):
                L[i] = L[i].rstrip()
                L[i] = int(L[i])
            M.append(L)
            ligne = m.readline()

        F = []
        for i in range(len(M)):
            k = i
            S = []
            for i in range(len(M)):
                l1 = M[k]
                l2 = M[i]
                n = 0
                s1 = 0
                s2 = 0
                for i in range(len(l1)):
                    n += l1[i] * l2[i]
                    s1 += l1[i] ** 2
                    s2 += l2[i] ** 2
                    r1 = sqrt(s1)
                    r2 = sqrt(s2)
                    d = r1 * r2
                R = round(n / d, 2)
                R2 = str(R)
                S.append(R2)
            F.append(S)

        copy = str()
        for i in F:
            l = i
            joindre = ' '.join(l)
            copy += joindre + '\n'


    with open("Similarite.txt","w") as m:
        m.write(copy)
    return F


def recommandation(a):
    with open("booksread.txt",'r')as b:
        F=similarite()
        B=dico_bookread()
        booksread=b.readlines()
        U=dico_user()
        BK=dico_books()
        L=B[a]
        l=[]
        M=[]
        copie2=str()
        copie=str()
        print(L[0]+',')
        print("Souhaitez-vous être affilié à un autre lecteur ? \n")
        print(" 1 - OUI \n 2 - NON \n")
        z=0
        while z<1 or z>2:
            z=int(input("Saisissez le numéro correspondant à votre choix:\n"))
        if z==1:

            for i in range(len(F)):
                if i == a-1:
                    l.append(0)
                else:
                    l.append(F[a-1][i])
            max = 0
            for i in range(len(l)):
                y=float(l[i])
                if y > max:
                    max=y
                    cle=i+1

            if max!=0:
                print(U[cle][0],'et vous avez des profils similaires ! Vous êtes compatible à', floor(max*100),'% !')
                print()

                livres_lu=B[cle]


                for i in livres_lu:
                    if i in L:
                        ind = livres_lu.index(i)
                        del livres_lu[ind]

                print("Voici les livres lu par",U[cle][0],"succeptibles de vous intéréssés :")
                print()
                k=0
                for i in range(1,len(livres_lu)):
                    e = int(livres_lu[i])
                    k+=1
                    print(k,' - ',BK[e])

                n=0
                while n<1 or n>4:
                    n=int(input('Saisissez le numéro du livre que vous souhaitez découvrir: \n'))

                L.append(livres_lu[n])
                nb = int(livres_lu[n])
                print()

            else:
                print("Malheuresement, vous n'êtes compatible à aucun lecteur !")
                time.sleep(6)
                menu_lecteur()

            texte = L[0]
            for i in range(1, len(L)):
                texte += ',' + L[i]
            texte += '\n'

            for i in range(len(booksread)):
                if i == a - 1:
                    copie += texte
                else:
                    copie += booksread[i]

            print('Le livre à bien été ajouter à votre bibliothèque ! ')
            print()
            print()
            print("Souhaitez-vous noter le livre ? \n 1 - OUI \n 2 - NON \n")
            verifi=0
            while verifi<1 or verifi > 2:
                verifi=int(input("Saisissez le numéro correspondant à votre choix :"))

            with open('matrice.txt','r') as m:
                if verifi == 1:
                    N=int(livres_lu[n])
                    print(BK[N])
                    note = 0
                    while note < 1 or note > 5:
                        note=int(input('Notez ce livre sur 5:'))

                    lignes = m.readline()
                    while lignes != "":
                        liste = lignes.split(' ')
                        for j in range(len(liste)):
                            liste[j] = liste[j].rstrip()
                        M.append(liste)
                        lignes = m.readline()

                    M[a-1][nb-1]=note

                    for i in M:
                        texte2 = str()
                        for j in i:
                            texte2 += str(j) + ' '
                        copie2 += texte2 + '\n'

                elif verifi==2:
                    print("N'oubliez pas de noter le livre un fois l'avoir lu ! ")
                    time.sleep(6)
                    menu_lecteur()
        else:
            menu_lecteur()

    with open("booksread.txt",'w') as br, open('matrice.txt','w') as m:
        br.write(copie)
        m.write(copie2)
