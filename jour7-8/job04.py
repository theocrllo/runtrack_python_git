def cesar(message, n):
    result = ""
    i = 0
    while i < len(message):
        print("avant modif",message[i])
        message[i] = message[i] - 3
        print("apres modif",message[i])

        i += 1
    return result


cesar("Bonjour tout le monde !", 3)
cesar("Abc xyz", -3)
