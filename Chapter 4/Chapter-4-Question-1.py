# Question 1

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

for i in range(5):
    draw_square(tess, 20)
    tess.penup()
    tess.forward(40)
    tess.pendown()
    
wn.mainloop()