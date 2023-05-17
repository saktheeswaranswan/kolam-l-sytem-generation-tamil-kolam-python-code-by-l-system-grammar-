import turtle

# L-System parameters
axiom = "A"
rules = {
    "A": "B+FA-FB-FB-FB-FA+B",
    "B": "BB"
}
angle = 45  # Angle in degrees
line_length = 10

# Function to expand the L-System string
def expand_lsystem_string(axiom, rules, iterations):
    result = axiom
    for _ in range(iterations):
        result = "".join([rules.get(ch, ch) for ch in result])
    return result

# Function to interpret the L-System string and draw the KAMBI Kolam pattern
def draw_kambi_kolam(lsystem_string, line_length):
    turtle.speed(0)  # Set the turtle's speed (0 is the fastest)

    # Set up the initial position
    turtle.penup()
    turtle.goto(-line_length, line_length)
    turtle.setheading(0)
    turtle.pendown()

    # Interpret the L-System string
    for symbol in lsystem_string:
        if symbol == "F":
            turtle.forward(line_length)
        elif symbol == "+":
            turtle.right(angle)
        elif symbol == "-":
            turtle.left(angle)

    turtle.done()  # Finish drawing

# Set the number of iterations
iterations = 20

# Expand the L-System string
lsystem_string = expand_lsystem_string(axiom, rules, iterations)

# Draw the KAMBI Kolam pattern
draw_kambi_kolam(lsystem_string, line_length)

