def arrondir_notes(notes):
    resultat = []
    for note in notes:
        if note >= 40:
            reste = note % 5
            if reste == 3 or reste == 4:
                note = note + 5 - reste
        resultat.append(note)
    return resultat


print(arrondir_notes([20, 38, 39, 40, 42, 43, 44, 82, 83, 99, 100]))
