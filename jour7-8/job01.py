def draw_rectangle(w, h):
    for ligne in range(h):
        if ligne == 0 or ligne == h - 1:
            print("|" + "-" * (w - 2) + "|")
        else:
            print("|" + " " * (w - 2) + "|")


draw_rectangle(10, 3)
