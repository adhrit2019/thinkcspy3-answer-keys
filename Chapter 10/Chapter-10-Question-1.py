# Question 1
import turtle

turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("Handling keypresses!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()

pensize = 1

def h1():
    tess.forward(30)
    

def h2():
    tess.left(45)
    

def h3():
    tess.right(45)
    

def h4():
    wn.bye()
    
    
def h5():
    tess.color("red")
    
    
def h6():
    tess.color("green")
    
    
def h7():
    tess.color("blue")
    
    
def h8():
    global pensize
    if pensize <= 20 and pensize >= 1:
        pensize += 1
        tess.pensize(pensize)
        
        
def h9():
    global pensize
    if pensize <= 20 and pensize >= 1:
        pensize -= 1
        tess.pensize(pensize)
        
        
def h10():
    wn.bgcolor("red")
    
    
def h11():
    wn.bgcolor("green")
    
    
def h12():
    wn.bgcolor("blue")
    
    
def h13():
    tess.backward(30)
    
    
wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "q")
wn.onkey(h5, "r")
wn.onkey(h6, "g")
wn.onkey(h7, "b")
wn.onkey(h8, "plus")
wn.onkey(h9, "minus")
wn.onkey(h10, "R")
wn.onkey(h11, "G")
wn.onkey(h12, "B")
wn.onkey(h13, "Down")
wn.listen()
wn.mainloop()