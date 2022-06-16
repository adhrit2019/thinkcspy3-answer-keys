# Question 4
import turtle

def draw_square(t, sz):
    for i in range(4):
        for j in range(4):
            t.forward(sz)
            t.left(90)
        t.right(90)
    

wn = turtle.Screen()
wn.bgcolor("lightgreen")
alex = turtle.Turtle()
alex.color("blue")
alex.pensize(3)

for i in range(5):
    alex.left(72)
    draw_square(alex, 50)
    
wn.mainloop()