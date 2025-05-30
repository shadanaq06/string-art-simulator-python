import turtle
import math

screen = turtle.Screen()
screen.bgcolor("Black")

# initializing turtle to create nails
nail = turtle.Turtle()
nail.shape('circle')
nail.color("pink")
nail.speed(2)

# initializing turtle to draw strings
string = turtle.Turtle()
string.color("red")
string.speed(2)

# input number of nails
num_nails = int(input("Enter the number of nails: "))

# initializing variables for storing the position of nails and total string length
prev_x = 0
prev_y = 0
initial_x = 0
initial_y = 0
string_length = 0

# Costs
nails_cost = 0.12
strings_cost = 0.07  # per meter
pixels = 32  # pixels per meter
board = 5.00

for i in range(num_nails):
    x = int(input('Enter the x-coordinate: '))
    y = int(input('Enter the y-coordinate: '))

    nail.penup()
    nail.goto(x, y)
    nail.stamp()

    if i == 0:
        initial_x, initial_y = x, y
    else:
        string.penup()
        string.goto(prev_x, prev_y)
        string.pendown()
        string.goto(x, y)

        # Add length between previous and current nail
        each_string_length = math.sqrt((x - prev_x) ** 2 + (y - prev_y) ** 2)
        string_length += each_string_length

    prev_x, prev_y = x, y

# Connect last nail to the first
string.penup()
string.goto(prev_x, prev_y)
string.pendown()
string.goto(initial_x, initial_y)

# Add final segment to string length
each_string_length = math.sqrt((initial_x - prev_x) ** 2 + (initial_y - prev_y) ** 2)
string_length += each_string_length

# Calculate costs
nails_cost_total = num_nails * nails_cost
strings_cost_total = (string_length / pixels) * strings_cost
final_cost = nails_cost_total + strings_cost_total + board

# Show cost
nail.penup()
nail.goto(-200, 200)
nail.color("purple")
nail.write(f"Your Total Cost is ${final_cost:.2f}", font=("Times New Roman", 18, "normal"))

screen.exitonclick()
