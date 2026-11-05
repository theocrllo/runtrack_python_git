def average(a, b, c):
    return (a + b + c) / 3


a = float(input("Entre la première note : "))
b = float(input("Entre la deuxième note : "))
c = float(input("Entre la troisième note : "))

moyenne_etudiant = average(a, b, c)

if moyenne_etudiant >= 15 and moyenne_etudiant <= 20:
    print("Très bon élève")
elif moyenne_etudiant >= 11 and moyenne_etudiant < 15:
    print("Bon élève")
elif moyenne_etudiant >= 8 and moyenne_etudiant < 11:
    print("Élève moyen")
elif moyenne_etudiant >= 0 and moyenne_etudiant < 8:
    print("Élève devant faire des efforts")
else:
    print("La moyenne doit être comprise entre 0 et 20")
