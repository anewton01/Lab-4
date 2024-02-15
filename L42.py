#the authors' names are Abby Newton and Sydney Eidelbes
import turtle
jack=turtle.Turtle()
jack.color("yellow")

for side in range(4):
    if side==1:
        jack.color("blue")
    jack.forward(100)
    jack.right(90)
else:
        jack.color("purple")
        jack.forward(100)
        jack.right(90)
