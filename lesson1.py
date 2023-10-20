from turtle import *
# we want to paimt house

#step 1: draw a square
speed(30)
width(7)
color("purple")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
#and of square
#drawing door
forward(70)
color("yellow")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
penup()
goto(0,150)
pendown()
color("blue")


right(240)


forward(40)
right(90)
forward(40)
right(90)
forward(40)
penup()
goto(200,150)
pendown()

forward(40)
left(90)
forward(40)
left(90)
forward(40)



exitonclick()

