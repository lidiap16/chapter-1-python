""" lidia pasiecznik 24.09.24
tasks 5"""

#task 5
import turtle
import random
scr=turtle.Screen()
scr.bgcolor("LIGHTBLUE")
# for i in range(0,4):
#     turtle.pencolor("green")
#     turtle.pensize(3)
#     turtle.forward(20)
#     turtle.penup()
#     turtle.forward(20)
#     turtle.pendown()
#     turtle.forward(20)
#     turtle.penup()
#     turtle.forward(20)
#     turtle.pendown()
#     turtle.right(90)
# 
# turtle.exitonclick()

#task 6
# for i in range(0, 3):
#     color = random.choice(["red","green","blue","purple","pink","orange"])
#     turtle.color(color)
#     turtle.begin_fill()
#     turtle.pendown()
#     for i in range(0,3):
#         turtle.forward(30)
#         turtle.left(120)
#     turtle.end_fill()
#     turtle.penup()
#     turtle.forward(50)
# turtle.exitonclick()


#task 7

for i in range(0, 25):
    turtle.pendown()
    line_lenght = random.randint(10,25)
    line_angle = random.randint(1,360)
    turtle.forward(line_lenght)
    turtle.right(line_angle)
    color = random.choice(["red","orange","yellow","green","blue","purple"])
    turtle.color(color)




