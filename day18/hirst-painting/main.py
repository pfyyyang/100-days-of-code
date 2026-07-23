# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(252, 250, 247), (253, 246, 250), (237, 251, 244), (248, 228, 25), (199, 11, 35), (233, 228, 4), (210, 13, 8), (197, 67, 21), (237, 244, 250), (232, 149, 47), (33, 92, 186), (41, 212, 78), (33, 30, 153), (16, 21, 56), (65, 9, 47), (242, 40, 141), (67, 201, 228), (61, 21, 11), (13, 206, 223), (220, 22, 108), (227, 164, 8), (16, 154, 23), (244, 61, 21), (98, 75, 10), (220, 139, 197), (248, 11, 8), (73, 240, 159), (5, 38, 33), (11, 98, 60), (74, 215, 151)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100


for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)






screen = turtle_module.Screen()
screen.exitonclick()