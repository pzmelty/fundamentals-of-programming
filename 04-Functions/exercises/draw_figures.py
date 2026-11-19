import turtle
from figures import draw_square
from figures import draw_triangle   
from figures import draw_rectangle
# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)

# Side length
side_length_a = 100
side_length_b = 200
# Draw a square
#for i in range(4):
 #   pen.forward(side_length)
  #  pen.right(90)

draw_square(pen, side_length_a)
pen.penup()
pen.goto(-200,100)
pen.pendown()
draw_square(pen, side_length_a)
pen.penup()
pen.goto(-400,100)
pen.pendown()
draw_triangle(pen, side_length_a)
pen.penup()
pen.goto(-600,100)
pen.pendown()
draw_triangle(pen, side_length_a)
pen.penup()
pen.goto(500,100)
pen.pendown()
draw_rectangle(pen, side_length_a, side_length_b)
pen.penup()
pen.goto(300,100)
pen.pendown()
draw_rectangle(pen, side_length_a, side_length_b)

# Hide the turtle and finish
pen.hideturtle()
window.mainloop()