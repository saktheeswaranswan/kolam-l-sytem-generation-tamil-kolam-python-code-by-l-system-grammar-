import cv2
import numpy as np
import turtle

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

# Function to interpret the L-System string and draw the SUZHI Kolam pattern
def draw_suzhi_kolam(lsystem_string, dot_size):
    turtle.speed(0)  # Set the turtle's speed (0 is the fastest)

    # Set up the initial position
    turtle.penup()
    turtle.goto(-dot_size, dot_size)
    turtle.pendown()

    # Draw the dots
    turtle.dot(dot_size)

    # Interpret the L-System string
    for symbol in lsystem_string:
        if symbol == "F":
            draw_line(dot_size)
        elif symbol == "A":
            draw_arc(dot_size, 90)
        elif symbol == "B":
            forward_units = 5 / (2 ** 0.5)
            turtle.forward(forward_units)
            draw_arc(forward_units, 270)
            turtle.dot(dot_size)

    turtle.done()  # Finish drawing

# Function to draw a line segment
def draw_line(length):
    turtle.forward(length)

# Function to draw an arc
def draw_arc(radius, angle):
    turtle.circle(radius, angle)

# Set the dot size and number of iterations
dot_size = 10
iterations = 2

# Expand the L-System string
lsystem_string = expand_lsystem_string(axiom, rules, iterations)

# Initialize video capture
video_capture = cv2.VideoCapture(0)

while True:
    # Read a frame from the video stream
    ret, frame = video_capture.read()

    # Draw the Suzhi Kolam pattern on the current frame
    draw_suzhi_kolam(lsystem_string, dot_size, frame)

    # Display the frame
    cv2.imshow('Live Video', frame)

    # Break the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close OpenCV windows
video_capture.release()
cv2.destroyAllWindows()
