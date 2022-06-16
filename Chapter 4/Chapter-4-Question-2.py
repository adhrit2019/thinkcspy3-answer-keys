# Question 2

import turtle

def draw_square(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)
        
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("HotPink")
tess.pensize(4)

size = 20
for i in range(5):
    draw_square(tess, size)
    tess.left(180)
    tess.penup()
    tess.forward(10)
    tess.left(90)
    tess.forward(10)
    tess.left(90)
    tess.pendown()
    size += 20
    
wn.mainloop()