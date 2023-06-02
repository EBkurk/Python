def addition():
    while True:
        try:

            num1 = float(input("Entrez un premier nombre : "))
            num2 = float(input("Entrez un deuxième nombre : "))
            
            result = num1 + num2
            
            print(f"Le résultat de l'addition de {num1} avec {num2} est égal à {result}")
            
            break
        
        except ValueError:

            print("Veuillez entrer deux nombres valides.")

addition()
