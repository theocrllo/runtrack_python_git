def distance_gardien(marches, hauteur):
    distance = marches * hauteur * 2 * 5 * 7 / 100
    print(f"Pour {marches} marches de {hauteur} cm, le gardien parcourt {distance:.2f} m par semaine.")


distance_gardien(100, 20)
