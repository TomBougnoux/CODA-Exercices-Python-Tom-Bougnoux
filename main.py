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
    number = int(input("Selectionner un autre nombre "))
    print("Votre résultat est", nombre + number)

def exercice6():
    nombre = int(input("Selectionner un nombre "))
    number = int(input("Selectionner un autre a soustraire "))
    print("Votre résultat est", nombre - number)

def exercice7():
    nombre = int(input("Selectionner un nombre "))
    number = int(input("Selectionner un autre a multiplier "))
    print("Votre résultat est", nombre * number)

def exercice8():
    nombre = int(input("Selectionner un nombre "))
    number = int(input("Selectionner un autre a diviser "))
    if number==0:
        print("On ne peut pas diviser par 0")
    else:
        print("votre résultat est", nombre / number)

def exercice9():
    nombre = int(input("Selectionner un nombre "))
    print("Votre résultat est", nombre * nombre)

def exercice10():
    nombre = int(input("Selectionner un nombre qui sera multiplier par 2 "))
    print("votre résultat est", nombre*2)

def exercice11():
    nombre = int(input("Selectionner un nombre qui sera diviser par 2 "))
    print("votre résultat est", nombre/2)

def exercice12():
    for i in range(5):
        print("ggs wp")

def exercice13():
     for i in range(1,6):
        print(i)

def exercice14():
   nombre=int(2)
   for i in range(1, 6):
    print(f"{i} x 2 =", nombre*i)

def exercice15():
    nombre = int(input("entrer la longueur d'un cote en centimetre "))
    print("le carre a une perimetre de", nombre * 4)

def exercice16():
    nombre = int(input("entrer la longueur d'un cote en centimetre "))
    print("le carre a une aire de", nombre * nombre)

def exercice17():
    nombre = int(input("entrer les euros "))
    print(nombre * 1.1, "dollars")

def exercice18():
    nombre = int(input("entrer les minutes "))
    print(nombre*60, "secondes")

def exercice19():
    nombre =int(input("entrer le prix HT "))
    print(nombre * 1.2, "TTC")

def exercice20():
    nom =(input("Quel est ton nom "))
    age =int(input("Quel est ton age "))
    print(nom,"a", age, "ans")

def exercice21():
    nombre =int(input("entrer le nombre "))
    if nombre == 0 :
        print("nul")
    elif nombre < 0 :
        print("négatif")        
    elif nombre > 0 :
        print("positif")








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
    elif choix == "6":
        exercice6()
    elif choix == "7":
        exercice7()
    elif choix =="8":
        exercice8()
    elif choix =="9":
        exercice9()
    elif choix =="10":
        exercice10()
    elif choix =="11":
        exercice11()
    elif choix =="12":
        exercice12()
    elif choix =="13":
        exercice13()
    elif choix =="14":
        exercice14()
    elif choix =="15":
        exercice15()
    elif choix =="16":
        exercice16()
    elif choix =="17":
        exercice17()
    elif choix =="18":
        exercice18()
    elif choix =="19":
        exercice19()
    elif choix =="20":
        exercice20()
    elif choix =="21":
        exercice21()
    else:
        print("Exercice non reconnu.")
if __name__ == "__main__":
    main()