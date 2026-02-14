from turtle import *

#making a house

#drawing a square
speed(10)
width(7)
color("red")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#end of square

#making a door

forward(70)
color("blue")
begin_fill()
left(90)
forward(120) #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

#end of making a door

#making a roof

penup()
goto(200, 200)
pendown ()

color("black")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#end of making a roof

#making a window N1

penup()
goto(0, 0)
pendown()

color("red")
right(150)
forward(130)
right(90)
color("yellow")
begin_fill()
forward (50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

#end of making window N1

#making a window N2

penup()
goto(200, 200)
pendown()

color("red")
left(90)
forward (25)
color ("yellow")
begin_fill()
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

#end of making window N2

exitonclick()