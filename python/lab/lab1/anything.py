#rainbowturtle


import turtle

shape = turtle.Turtle()

rainbow = ["red", "orange", "yellow", "green", "blue", "purple"]

# Write whatever code you want here!
shape.penup()
shape.back(50)
shape.pendown()
shape.width(5)



for prettycolor in rainbow:
   shape.color(prettycolor)

   shape.forward(100)
   shape.right(60)
shape.hideturtle()
