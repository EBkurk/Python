import random

def jouer():
    joueur_vie = 50
    ennemi_vie = 50
    joueur_potions = 3
    
    print("Bienvenue dans le jeu de rôle !")
    
    while joueur_vie > 0 and ennemi_vie > 0:
        print(f"Points de vie du joueur : {joueur_vie}")
        print(f"Points de vie de l'ennemi : {ennemi_vie}")
        
        choix = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")
        
        if choix == "1":
            degats = random.randint(5, 10)
            ennemi_vie -= degats
            print(f"Vous infligez {degats} points de dégâts à l'ennemi.")
        elif choix == "2":
            if joueur_potions > 0:
                soins = random.randint(15, 50)
                joueur_vie += soins
                joueur_potions -= 1
                print(f"Vous récupérez {soins} points de vie.")
            else:
                print("Vous n'avez plus de potions.")
                continue
        else:
            print("Choix invalide. Veuillez choisir 1 pour attaquer ou 2 pour utiliser une potion.")
            continue
        
        if ennemi_vie <= 0:
            print("Félicitations ! Vous avez gagné la partie.")
            break
        
        attaque_ennemi = random.randint(5, 15)
        joueur_vie -= attaque_ennemi
        print(f"L'ennemi vous inflige {attaque_ennemi} points de dégâts.")
        
        if joueur_vie <= 0:
            print("Vous avez perdu la partie.")
    
    print("Fin du jeu.")
 
jouer()
