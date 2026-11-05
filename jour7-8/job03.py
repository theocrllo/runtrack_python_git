def tapis(n):
    print("+" + "-" * (n + 1) + "+")
    for ligne in range(n + 1):
        contenu = ""
        for colonne in range(n + 1):
            if colonne == n - ligne:
                contenu = contenu + " "
            else:
                contenu = contenu + "#"
        print("|" + contenu + "|")
    print("+" + "-" * (n + 1) + "+")


tapis(10)
