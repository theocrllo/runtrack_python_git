hauteur = int(input("Entre la hauteur du triangle : "))

for ligne in range(hauteur):
    espaces = " " * (hauteur - ligne - 1)
    if ligne == hauteur - 1:
        print(espaces + "/" + "_" * (ligne * 2) + "\\")
    else:
        print(espaces + "/" + " " * (ligne * 2) + "\\")
