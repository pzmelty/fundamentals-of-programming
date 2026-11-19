###
# Draw a square
#
import turtle
def draw_square(length):
    for i in range(4):
        turtle.forward(length)
        turtle.right(90)