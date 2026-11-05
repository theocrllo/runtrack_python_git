def is_odd(nb):
    if type(nb) != int:
        print("Le nombre doit être un entier positif")
    elif nb < 0:
        print("Le nombre doit être un entier positif")
    elif nb % 2 == 0:
        print("pair")
    else:
        print("impair")


is_odd(4)
is_odd(7)
is_odd(0)
is_odd(-3)
is_odd(2.5)
is_odd("bonjour")
