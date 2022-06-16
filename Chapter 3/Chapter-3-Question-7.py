# Question 7

import turtle

wn = turtle.Screen()
pirate = turtle.Turtle()
wn.bgcolor("peach puff")
pirate.shape("turtle")

for turn in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
    pirate.left(turn)
    pirate.forward(100)
    
wn.mainloop()