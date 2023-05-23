import turtle

# Function to draw a straight line segment
def draw_line(length):
    turtle.forward(length)

# Function to draw a curved line segment
def draw_curve(radius, angle):
    turtle.circle(radius, angle)

# Function to draw a square loop kolam pattern
def draw_kolam():
    turtle.speed(0)  # Set the turtle's speed (0 is the fastest)

    # Set up the initial position
    turtle.penup()
    turtle.goto(-100, 100)
    turtle.pendown()

    # Draw the square loop kolam pattern
    draw_line(200)
    draw_curve(100, 90)
    draw_line(200)
    draw_curve(100, 90)
    draw_line(200)
    draw_curve(100, 90)
    draw_line(200)
    draw_curve(100, 90)

    turtle.done()  # Finish drawing

# Draw the kolam pattern
draw_kolam()

