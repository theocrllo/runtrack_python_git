montant = 10000
taux = 5

print("Montant initial :", montant, "euros")
print("Taux de rendement annuel :", taux, "%")
print("Gain annuel :", montant * taux / 100, "euros")

montant = montant + 5000
taux = taux + 2

print("Nouveau montant :", montant, "euros")
print("Nouveau taux de rendement :", taux, "%")
print("Nouveau gain annuel :", montant * taux / 100, "euros")

montant = montant - montant * 10 / 100
taux = taux - 1

print("Montant final :", montant, "euros")
print("Taux final :", taux, "%")
print("Gain final :", montant * taux / 100, "euros")
