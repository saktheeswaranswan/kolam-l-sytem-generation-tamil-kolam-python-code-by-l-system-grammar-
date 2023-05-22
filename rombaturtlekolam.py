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
def draw_suzhi_kolam(lsystem_string, dot_size, rhombus_size):
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

# Prompt the user to enter the dot size and rhombus size
dot_size = int(input("Enter the dot size: "))
rhombus_size = int(input("Enter the rhombus size: "))

# Set the number of iterations based on the rhombus size
iterations = rhombus_size

# Expand the L-System string
lsystem_string = expand_lsystem_string(axiom, rules, iterations)

# Draw the SUZHI Kolam pattern within the rhombus
draw_suzhi_kolam(lsystem_string, dot_size, rhombus_size)

