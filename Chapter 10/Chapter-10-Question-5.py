# Question 4
import turtle

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()

def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()
    tess.hideturtle()
    

draw_housing()

green = turtle.Turtle()
green.shape("circle")
green.shapesize(3)
green.fillcolor("dark grey")
green.hideturtle()

orange = turtle.Turtle()
orange.shape("circle")
orange.shapesize(3)
orange.fillcolor("dark grey")
orange.hideturtle()

red = turtle.Turtle()
red.shape("circle")
red.shapesize(3)
red.fillcolor("dark grey")
red.hideturtle()

green.penup()
green.forward(40)
green.left(90)
green.forward(50)

orange.penup()
orange.forward(40)
orange.left(90)
orange.forward(120)

red.penup()
red.forward(40)
red.left(90)
red.forward(190)

green.showturtle()
green.fillcolor("green")
orange.showturtle()
red.showturtle()

# This variable holds the current state of the machine
state_num = 0

def advance_state_machine():
    global state_num
    
    if state_num == 0:
        green.fillcolor("green")
        orange.fillcolor("orange")
        state_num = 1
        
    elif state_num == 1:                      # Transition from state 0 to state 1
        green.fillcolor("dark grey")
        orange.fillcolor("orange")
        state_num = 2
    
    elif state_num == 2:                    # Transition from state 1 to state 2
        orange.fillcolor("dark grey")
        red.fillcolor("red")
        state_num = 3
    
    else:                                   # Transition from state 2 to state 0
        red.fillcolor("dark grey")
        green.fillcolor("green")
        state_num = 0


wn.ontimer(advance_state_machine, 3000)
wn.ontimer(advance_state_machine, 4000)
wn.ontimer(advance_state_machine, 6000)
wn.ontimer(advance_state_machine, 7000)

wn.listen()
wn.mainloop()