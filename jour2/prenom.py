"""""
prenom = input("Entrez le nom d'un élève : ")

if prenom == "Théo":
    print("ah oui je me souviens de toi ", prenom, " !")
elif prenom == "eleve":
    print("salut eleve")
elif prenom == "eleve2":
    print("salut", prenom)
else:
    print("qui es tu ?")
    
    
"""
prenom = "Théo"
"""""
match prenom:
    case "Théo":
        print("bonjour théo")

if prenom == "eleve" or "eleve2" or "eleve3":
    print("Bonjour les eleves !")

"""

if prenom :
    print("Bonjour", prenom)