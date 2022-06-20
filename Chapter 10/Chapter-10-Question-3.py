# Question 3
import turtle                                   # Tess becomes a traffic light.

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
green.fillcolor("green")
green.hideturtle()

orange = turtle.Turtle()
orange.shape("circle")
orange.shapesize(3)
orange.fillcolor("orange")
orange.hideturtle()

red = turtle.Turtle()
red.shape("circle")
red.shapesize(3)
red.fillcolor("red")
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

# A traffic light is a kind of state machine with three states,
# Green, Orange, Red. We number these states 0, 1, 2
# When the machine changes state, we change tess’ position and
# her fillcolor.

# This variable holds the current state of the machine
state_num = 0

def advance_state_machine():
    global state_num
    
    if state_num == 0:                      # Transition from state 0 to state 1
        green.hideturtle()
        orange.showturtle()
        state_num = 1
    
    elif state_num == 1:                    # Transition from state 1 to state 2
        orange.hideturtle()
        red.showturtle()
        state_num = 2
    
    else:                                   # Transition from state 2 to state 0
        red.hideturtle()
        green.showturtle()
        state_num = 0


wn.onkey(advance_state_machine, "space")

wn.listen()
wn.mainloop()