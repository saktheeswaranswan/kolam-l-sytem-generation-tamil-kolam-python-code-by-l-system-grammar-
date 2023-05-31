from turtle import *
from math import sqrt

def main():
    pensize(4)
    n = numinput('L system kolam', 'Enter level: ')
    lt(45)
    ht()
    state = 'FBFBFBFB'  # Axiom or Initiator
    for _ in range(int(n)):
        final_state = ''
        for character in state:
            if character == 'F':
                final_state += character  # Rule A: A -> AFBFA
            elif character == 'A':
                final_state += 'AFBFA'  # Rule B: B -> AFBFBFBFA
            elif character == 'B':
                final_state += 'AFBFBFBFA'
        state = final_state
    
    speed(0)  # Set the turtle's speed to the fastest
    
    # Define the bounds of the cross-like polygon
    bounds = [(0, 0), (0, 200), (200, 200), (200, 0)]
    
    # Draw the boundary polygon
    color("black")
    begin_fill()
    for vertex in bounds:
        goto(vertex)
    goto(bounds[0])
    end_fill()
    
    # Start the turtle at the center of the polygon
    penup()
    start_x = (bounds[0][0] + bounds[2][0]) / 2
    start_y = (bounds[0][1] + bounds[2][1]) / 2
    goto(start_x, start_y)
    setheading(0)
    pendown()
    
    for character in state:
        if character == 'F':
            color("green")
            begin_fill()
            fd(20)  # Forward 10 units
            delay(40)
        elif character == 'A':
            color("blue")
            arc(20, 90)  # Draw an arc (circle(10, 90))
            delay(40)
        elif character == 'B':
            color("red")
            I = 10 / sqrt(2)  # Calculate forward units
            fd(I)  # Forward I units
            arc(I, 270)  # Draw an arc (circle(I, 270))
            fd(I)  # Forward I units
            delay(40)
        end_fill()

    return "done"

def arc(radius, angle):
    left(90)
    circle(radius, angle)

if __name__ == '__main__':
    msg = main()
    print(msg)
    mainloop()

