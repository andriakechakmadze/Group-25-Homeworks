from turtle import *

#we want to draw a house

#step 1: draw a square
speed(70)
width(7)
color("blue")
forward(200) 
left(90)

forward(200) 
left(90) 

forward(200) 
left(90)

forward(200) 
left(90) 
#end of square

#draw a door

forward(70) 
color("yellow") 
begin_fill()
left(90)
forward(120) #heigt of the door
right(90)
forward(60)
right(90)
forward(120) 
end_fill()

penup()
goto(200, 200) 
pendown ()

color("red") 
begin_fill()
right(150) 
forward(200)
left(120) 
forward(200)
end_fill()

penup() 
goto(50, 100) 
pendown() 

color("red")
right(60)
forward(30) 
right(90) 
forward(30) 
right(90) 
forward(30) 
right(90)
forward(30) 

penup()
goto(150, 100)
pendown()

left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30) 

penup()
goto(200, 200)
pendown()

left(90) 
forward(200)
right(90)
forward(200)
right(90)
forward(200) 

penup()
goto(300, 200)
pendown()

right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)


penup()
goto(400, 200)
pendown()

right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(25)

penup()
goto(270, 200)
pendown()

left(180)
forward(30)
left(90)
forward(30)
left(90)
forward(30)


penup()
goto(0, 200)
pendown() 

right(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)

penup()
goto(-200, 200)
pendown()

left(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)

penup()
goto(-130, 200)
pendown()

left(180)
forward(30)
right(90)
forward(30)
right(90)
forward(30)

penup()
goto(-50, 200)
pendown()

left(180)
forward(30)
right(90)
forward(30)
right(90)
forward(30)

penup()
goto(100,360)
pendown()

left(180)
forward(100)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)



exitonclick()