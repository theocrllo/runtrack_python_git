def inverser(texte):
    resultat = ""
    for i in texte:
        resultat = i + resultat
    return resultat


print(inverser("nikana"))
