# Question 9

import turtle

def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()
    
    if height > 0:
        t.left(90)
        t.forward(height)
        t.write(" " + str(height))
        t.right(90)
        t.forward(40)
        t.right(90)
        t.forward(height)
        t.left(90)
        
    elif height < 0:
        t.right(90)
        t.forward(height * -1)
        t.penup()
        t.forward(15)
        t.write(" " + str(height))
        t.backward(15)
        t.pendown()
        t.left(90)
        t.forward(40)
        t.left(90)
        t.forward(height * -1)
        t.right(90)
        
    t.end_fill()
    t.forward(10)
    
wn = turtle.Screen()
wn.bgcolor("lightgreen") # Set up the window and its attributes

tess = turtle.Turtle()
tess.color("blue", "red")
tess.pensize(3) # Create tess and set some attributes

xs = [48, 117, -200, 240, 160, -250, 220, -47, 200]

for a in xs:
    draw_bar(tess, a)

wn.mainloop()