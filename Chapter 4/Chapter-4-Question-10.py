# Question 9

import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.pensize(4)
tess.color("HotPink")

def make_star(t, sz):
    for i in range(5):
        t.forward(100)
        t.right(144)
        
for i in range(5):
    make_star(tess, 100)
    tess.penup()
    tess.forward(350)
    tess.right(144)
    tess.pendown()

wn.mainloop()