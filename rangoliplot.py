import turtle

def draw_circle(radius, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_rangoli():
    turtle.speed(10)

    # Create the first circle
    draw_circle(245, '#17327F')
    draw_circle(235, '#FFD506')

    # Decorate the edges of the first circle
    draw_circle(205, '#FA0008')
    draw_circle(195, '#FA0008')
    draw_circle(195, '#FFFFFF')
    draw_circle(185, '#FA0008')
    draw_circle(185, '#FFFFFF')

    # Create the second circle
    turtle.penup()
    turtle.goto(0, -35)
    turtle.pendown()
    draw_circle(150, '#FA0008')
    draw_circle(140, '#FFFFFF')

    # Decorate the second circle
    draw_circle(110, '#1E94FF')
    draw_circle(100, '#1E94FF')

    # Create the third circle
    turtle.penup()
    turtle.goto(0, -65)
    turtle.pendown()
    draw_circle(70, '#010147')

    # Decorate the third circle
    draw_circle(40, '#1E94FF')

    # Create the speech bubble and background
    turtle.penup()
    turtle.goto(0, -220)
    turtle.pendown()
    turtle.fillcolor('#FFFFFF')
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(290)
        turtle.left(90)
        turtle.forward(55)
        turtle.left(90)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(-30, -170)
    turtle.pendown()
    turtle.fillcolor('#1E94FF')
    turtle.begin_fill()
    turtle.goto(0, -120)
    turtle.goto(30, -170)
    turtle.goto(-30, -170)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(-120, 60)
    turtle.pendown()
    turtle.color('#1E94FF')
    turtle.write("ABCD", align="center", font=("Baker Street Inline", 270, "normal"))

    turtle.hideturtle()
    turtle.done()

# Run the draw_rangoli function
draw_rangoli()

