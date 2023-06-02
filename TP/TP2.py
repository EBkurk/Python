def ajouter_element(liste):
    element = input("Entrez l'élément à ajouter : ")
    liste.append(element)
    print(f"L'élément '{element}' a été ajouté à la liste de courses.")

def retirer_element(liste):
    element = input("Entrez l'élément à retirer : ")
    if element in liste:
        liste.remove(element)
        print(f"L'élément '{element}' a été retiré de la liste de courses.")
    else:
        print(f"L'élément '{element}' n'est pas présent dans la liste de courses.")

def afficher_liste(liste):
    print("Liste de courses :")
    for element in liste:
        print("- " + element)

def vider_liste(liste):
    liste.clear()
    print("La liste de courses a été vidée.")

def menu():
    liste_courses = []
    
    while True:
        print("\n--- MENU ---")
        print("1. Ajouter un élément")
        print("2. Retirer un élément")
        print("3. Afficher les éléments")
        print("4. Vider la liste")
        print("5. Quitter")
        
        choix = input("Entrez votre choix (1-5) : ")
        
        if choix == "1":
            ajouter_element(liste_courses)
        elif choix == "2":
            retirer_element(liste_courses)
        elif choix == "3":
            afficher_liste(liste_courses)
        elif choix == "4":
            vider_liste(liste_courses)
        elif choix == "5":
            print("Merci d'avoir utilisé le programme. Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez entrer un nombre entre 1 et 5.")

menu()
