import cv2
import numpy as np
import turtle
import time

# L-System parameters
axiom = "FBFBFBFB"  # Initiator
rules = {
    "A": "AFBFA",
    "B": "AFBFBFBFA"
}
angle = 45  # Angle in degrees

# Function to expand the L-System string
def expand_lsystem_string(axiom, rules, iterations):
    result = axiom
    for _ in range(iterations):
        result = "".join([rules.get(ch, ch) for ch in result])
    return result

# Function to interpret the L-System string and draw the Kambi Kolam pattern
def draw_kambi_kolam(lsystem_string, dot_size, rhombus_size):
    turtle.speed(100)  # Set the turtle's speed (10 is a faster speed)

    # Calculate the side length of the rhombus based on the dot size and rhombus size
    rhombus_side = rhombus_size * dot_size

    # Set up the initial position
    turtle.penup()
    turtle.goto(-rhombus_side / 2, rhombus_side / 2)
    turtle.pendown()

    # Interpret the L-System string
    for symbol in lsystem_string:
        if symbol == "F":
            draw_line(dot_size, "red")
        elif symbol == "A":
            draw_arc(dot_size, 90, "green")
        elif symbol == "B":
            forward_units = 5 / (2 ** 0.5)
            turtle.forward(forward_units)
            draw_arc(forward_units, 270, "green")

    turtle.done()  # Finish drawing

# Function to draw a line segment
def draw_line(length, color):
    turtle.color(color)
    turtle.forward(length)

# Function to draw an arc
def draw_arc(radius, angle, color):
    turtle.color(color)
    turtle.circle(radius, angle)

# Prompt the user to enter the dot size and rhombus size
dot_size = int(input("Enter the dot size: "))
rhombus_size = int(input("Enter the rhombus size: "))

# Set the number of iterations based on the rhombus size
iterations = rhombus_size

# Expand the L-System string
lsystem_string = expand_lsystem_string(axiom, rules, iterations)

# Draw the Kambi Kolam pattern within the rhombus
draw_kambi_kolam(lsystem_string, dot_size, rhombus_size)

# Get the x,y coordinates of the polygon
polygon_coordinates = []
for i in range(3):
    x, y = input("Enter the x and y coordinates of the polygon vertex {}: ".format(i + 1))
    polygon_coordinates.append((x, y))

# Draw the polygon
turtle.penup()
turtle.goto(polygon_coordinates[0])
turtle.pendown()
for i in range(len(polygon_coordinates) - 1):
    turtle.goto(polygon_coordinates[i + 1])

# Draw the kolam within the polygon
turtle.penup()
turtle.goto(polygon_coordinates[0])
turtle.pendown()
draw_kambi_kolam(lsystem_string, dot_size, rhombus_size)

# Start the live video stream
turtle.show()

# Loop forever, drawing the kolam in the live video stream
while True:
    # Get the current frame from the video stream
    frame = cv2.imread("frame.jpg")

    # Convert the frame to grayscale
    grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Threshold the grayscale frame to create a binary image
    threshold_image = cv2.threshold(grayscale_frame, 127, 255, cv2.THRESH_BINARY)


