from turtle import*
from math import*

title("Draw Ensign")

l_star_yellow = 100
height = l_star_yellow*sin(radians(72))
rectangle_red = Turtle()
rectangle_red.speed(0)
rectangle_red.shape("blank")
rectangle_red.color("red", "red")
rectangle_red.begin_fill()
for _ in range(2):
	rectangle_red.forward(3*height)
	rectangle_red.left(90)
	rectangle_red.forward(2*height)
	rectangle_red.left(90)
rectangle_red.end_fill()


star_yellow = Turtle()
star_yellow.speed(0)
star_yellow.shape("blank")

star_yellow.penup()
star_yellow.forward(height + 18)
star_yellow.left(90)
star_yellow.forward(height/2 + 6)
star_yellow.right(90)
star_yellow.pendown()

star_yellow.color("yellow","yellow")

star_yellow.begin_fill()
star_yellow.left(72)
star_yellow.forward(l_star_yellow)
for _ in range(4):
	star_yellow.right(144)
	star_yellow.forward(l_star_yellow)
star_yellow.end_fill()

mainloop()