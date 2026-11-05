n = int(input("Entrez un entier : "))

for i in range(1, n + 1):
    print("Table de multiplication de", i)
    for j in range(1, 11):
        print(i * j)
    print()
