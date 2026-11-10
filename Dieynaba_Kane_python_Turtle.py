import turtle

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")

couleurs = ["cyan", "magenta", "yellow", "orange", "red"]

def polygone(cote, nb_cotes):
    for i in range(nb_cotes):
        t.forward(cote)
        t.left(360 / nb_cotes)

def couche(cote, nb_cotes, nb_copies):
    for i in range(nb_copies):
        t.color(couleurs[i % len(couleurs)])
        polygone(cote, nb_cotes)
        t.left(360 / nb_copies)

couche(100, 4, 8)     # couche 1 : 8 carrés
couche(140, 3, 6)     # couche 2 : 6 triangles
t.left(22.5)
couche(50, 4, 8)      # couche 3 : 8 petits carrés décalés
t.right(22.5)
couche(60, 6, 6)      # couche 4 : 6 hexagones
couche(80, 3, 12)     # couche 5 : 12 triangles
couche(70, 5, 10)     # couche 6 : 10 pentagones
couche(120, 4, 12)    # couche 7 : 12 grands carrés

turtle.done()