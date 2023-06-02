import random

def jeu_deviner_nombre():
    nombre_mystere = random.randint(0, 100)
    nombre_essais = 5
    
    print("Bienvenue dans le jeu de deviner le nombre mystère !")
    print(f"Vous avez {nombre_essais} essais pour trouver le nombre mystère compris entre 0 et 100.")
    
    for essai in range(1, nombre_essais + 1):
        nombre_choisi = int(input("Entrez un nombre : "))
        
        if nombre_choisi < nombre_mystere:
            print("Le nombre mystère est plus grand.")
        elif nombre_choisi > nombre_mystere:
            print("Le nombre mystère est plus petit.")
        else:
            print(f"Félicitations ! Vous avez trouvé le nombre mystère en {essai} essais.")
            return
    
    print(f"Dommage ! Vous n'avez pas trouvé le nombre mystère en {nombre_essais} essais.")
    print(f"Le nombre mystère était : {nombre_mystere}")

jeu_deviner_nombre()
