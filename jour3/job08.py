a = int(input("Entrez la longueur a : "))
b = int(input("Entrez la longueur b : "))
c = int(input("Entrez la longueur c : "))
if a == b and a == c and b == c :
    print("le triangle est equilateral")
elif a == b and b==c or c == a and c==b :
    print("le triangle est isocele")
elif c>b and c>a :
    print("le triangle est rectangle")
else:
    print("ce n'est aucun des trois triangles")