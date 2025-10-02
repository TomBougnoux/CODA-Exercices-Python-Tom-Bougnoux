def exercice1():
    print("Exercice 1 : Bonjour le monde !")
    print("Hello World !")

def exercice2():
    prenom = input("Quel est votre prenom")
    print("bonjour", prenom, "!")

def exercice3():
    print("premiere ligne")
    print("deuxieme ligne")
    print("troisieme ligne")

def exercice4():
    age = int(input("Quel est ton année de naissance"))
    print("Vous avez",2025-age,"ans")

def exercice5():
    nombre = int(input("Selectionner un nombre "))
    number =   int(input("Selectionner un autre nombre "))
    print("Votre résultat est", nombre + number)




def main():
    # Demande à l'utilisateur quel exercice exécuter
    choix = input("Entrez le numéro de l'exercice à exécuter : ")
    if choix == "1":
        exercice1()
    elif choix == "2":
        exercice2()
    elif choix == "3":
        exercice3()
    elif choix == "4":
        exercice4()
    elif choix == "5":
        exercice5()
    else:
        print("Exercice non reconnu.")
if __name__ == "__main__":
    main()