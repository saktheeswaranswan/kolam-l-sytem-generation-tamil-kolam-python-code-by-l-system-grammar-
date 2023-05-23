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

    # Set up the turtle
    turtle.penup()
    turtle.goto(-dot_size, dot_size)
    turtle.pendown()

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

    turtle.done()  # Finish drawing

# Function to draw a line segment
def draw_line(length):
    turtle.forward(length)

# Function to draw an arc
def draw_arc(radius, angle):
    turtle.circle(radius, angle)

# Set the dot size and number of iterations
dot_size = 10
iterations = 6

# Expand the L-System string
lsystem_string = expand_lsystem_string(axiom, rules, iterations)

# Set up the turtle screen
screen = turtle.Screen()
screen.tracer(0)  # Turn off animation updates

# Draw the SUZHI Kolam pattern
draw_suzhi_kolam(lsystem_string, dot_size)

# Calculate the required screen size based on the dot size and iterations
canvas_size = dot_size * (2 ** (iterations - 1))
screen_width = canvas_size + 100
screen_height = canvas_size + 100

# Update the screen size to fit the entire kolam
screen.screensize(screen_width, screen_height)

# Refresh the screen to show the entire kolam
screen.update()

# Keep the turtle graphics window open until closed by the user
turtle.mainloop()

