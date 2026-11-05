def what_to_eat(type, season):
    if type == "fruits" and season == "hiver":
        print("orange, mandarine et kiwi")
    elif type == "fruits" and season == "été":
        print("Poire, fraise, cassis")
    elif type == "légume" and season == "hiver":
        print("carotte, topinambour, endive")
    elif type == "légume" and season == "été":
        print("artichaut, aubergine,navet")


what_to_eat("fruits", "hiver")
what_to_eat("fruits", "été")
what_to_eat("légume", "hiver")
what_to_eat("légume", "été")
