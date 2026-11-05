L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
grand = L[0]
petit = L[0]

for nb in L:
    if nb > grand:
        grand = nb
    if nb < petit:
        petit = nb

print("la valeur max est :", grand)
print("la valeur min est :", petit)
