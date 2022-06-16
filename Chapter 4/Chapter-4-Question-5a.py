# Question 4

import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue")
tess.pensize(2)

def spiral(t, deg, num):
    t.right(deg)
    sz = 2
    for i in range(num):
        t.forward(sz)
        t.right(deg)
        sz += 2
        
spiral(tess, 90, 99)

wn.mainloop()
        