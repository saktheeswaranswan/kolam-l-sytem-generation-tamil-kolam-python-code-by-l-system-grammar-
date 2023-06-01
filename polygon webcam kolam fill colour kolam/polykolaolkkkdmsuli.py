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
    penup()
    goto(bounds[0])
    pendown()
    for vertex in bounds:
        goto(vertex)
    goto(bounds[0])
    
    for character in state:
        if character == 'F':
            color("green")
            if is_within_bounds(position(), bounds):
                fd(20)  # Forward 10 units
            else:
                break  # Stop drawing if outside the boundary
            delay(40)
        elif character == 'A':
            color("blue")
            if is_within_bounds(position(), bounds):
                circle(20, 90)  # Draw an arc (circle(10, 90))
            else:
                break  # Stop drawing if outside the boundary
            delay(40)
        elif character == 'B':
            color("red")
            I = 10 / sqrt(2)  # Calculate forward units
            if is_within_bounds(position(), bounds):
                fd(I)  # Forward I units
                circle(I, 270)  # Draw an arc (circle(I, 270))
                fd(I)  # Forward I units
            else:
                break  # Stop drawing if outside the boundary
            delay(40)

    return "done"

def is_within_bounds(pos, bounds):
    x, y = pos
    x_min, y_min = bounds[0]
    x_max, y_max = bounds[2]
    return x_min <= x <= x_max and y_min <= y <= y_max

if __name__ == '__main__':
    msg = main()
    print(msg)
    mainloop()

