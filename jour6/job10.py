L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
produit = 1

for nb in L:
    if nb >= 25 and nb <= 90:
        produit = produit * nb

print(produit)
