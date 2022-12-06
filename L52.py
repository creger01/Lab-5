# the authors names are: Cadyn and Sarah
import turtle

riley = turtle.Turtle()
riley.width(5)
riley.speed(0)

mood = input("how are you feeling? \n")
def draw_star(color):
    for side in range(5):
        riley.forward(100)
        riley.right(144)
        riley.color(color)




if mood == "happy":
    color = "pink"
elif mood == "sad":
    color = "blue"
elif mood == "sleepy":
    color = "green"
else:
    color = "red"

draw_star(color)
