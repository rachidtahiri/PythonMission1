
n= input("ecrire un nombre entier n ") # n est le nombre des objets
n=int(n)  # pour modifier 'n' à un nombre entier
p= input("donner un nombre de tirage p ")
p=int(p)   # pour modifier 'p' à un nombre entier
if p>n:    # si le nombre de tirage 'p' superieur au nombre total des objets il n'y aucune probabilité
    print("le nombre des permutations P=0") 
    print("le nombre des arrangements A=0")
    print("le nombre des combinaisons C=0")
else:
    Fn=1                                     # renitialisation de factoriel de 'n'
    i=n                                      # renitialisation de compteur 'i' 
    while i >=1:
        Fn=Fn*i
        i=i-1                                # decrimentation de compteur 'i'

    Fp=1                                     # renitialisation de factoriel de 'p'                              
    i=p                                      # renitialisation de compteur 'i'
    while i>=1:
        Fp=Fp*i
        i=i-1                                # decrimentation de compteur 'i'

    Fpn=1                                    # renitialisation de factoriel de ( n-p) Fpn
    i=n-p
    while i>=1:
        Fpn=Fpn*i
        i=i-1

    P=Fn
    A=Fn//Fpn
    C=A//Fp
             # affichage des resultats
    print("le nombre de permutation est P= : ",P)
    print("le nombre des arrangements est A= : ",A)
    print("le nombre des combinaisons est C= : ",C)

    