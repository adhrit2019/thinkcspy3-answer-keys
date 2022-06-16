# Question 8

import turtle

def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    if height >= 200:
        t.color("blue", "red")
        
    elif height >= 100 and height < 200:
        t.color("blue", "yellow")
        
    elif height < 100:
        t.color("blue", "green")
    
    t.begin_fill()
    # Added this line
    t.left(90)
    t.forward(height)
    t.write(" " + str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    t.forward(10)
    
wn = turtle.Screen()
wn.bgcolor("lightgreen") # Set up the window and its attributes

tess = turtle.Turtle()
tess.color("blue", "red")
tess.pensize(3) # Create tess and set some attributes

xs = [48,117,200,240,160,260,220]

for a in xs:
    draw_bar(tess, a)

wn.mainloop()