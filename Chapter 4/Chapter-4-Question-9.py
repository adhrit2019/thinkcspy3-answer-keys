# Question 9

import turtle
wn = turtle.Screen()
tess = turtle.Turtle()
tess.pensize(4)

def make_star(t, sz):
    t.left(36)
    for i in range(5):
        t.forward(100)
        t.left(144)
        
make_star(tess, 100)

wn.mainloop()