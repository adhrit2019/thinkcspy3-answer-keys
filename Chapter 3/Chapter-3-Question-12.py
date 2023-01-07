# Question 11

import turtle

wn = turtle.Screen()
t = turtle.Turtle()
wn.bgcolor("lightgreen")
t.shape("turtle")
t.color("blue")
t.pensize(4)

t.penup()

for i in range(12):
    t.forward(150)
    t.pendown()
    t.forward(20)
    t.penup()
    t.forward(15)
    t.stamp()
    t.backward(180)
    t.left(30)

wn.mainloop()