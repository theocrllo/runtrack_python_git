nom = "Clavier"
prix = 25.0
quantite = 40

print("Produit :", nom)
print("Prix unitaire :", prix, "euros")
print("Quantite en stock :", quantite)

achat = int(input("Quelle quantite de produits souhaitez-vous acheter ? "))

quantite = quantite - achat

prix = prix + prix * 10 / 100

print("Produit :", nom)
print("Prix unitaire :", prix, "euros")
print("Quantite en stock :", quantite)
