#!/bin/python3

import turtle
elsa = turtle.Turtle()
turtle.Screen().bgcolor("#ECEFF8")
elsa.color("#78ADCE")
for i in range(10):
    for i in range(2):
        elsa.forward(100)
        elsa.right(60)
        elsa.forward(100)
        elsa.right(120)
    elsa.right(36)

elsa.hideturtle()
turtle.getscreen()._root.mainloop()