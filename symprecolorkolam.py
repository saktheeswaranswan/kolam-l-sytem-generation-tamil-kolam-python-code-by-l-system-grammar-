from turtle import *
from math import sqrt
import random

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
                final_state += 'AB'  # Rule A: A -> AB
            elif character == 'A':
                final_state += 'AFBFA'  # Rule B: B -> AFBFA
            elif character == 'B':
                final_state += 'AFBFBFBFA'
        state = final_state
    
    speed(0)  # Set the turtle's speed to the fastest
    
    begin_fill()  # Begin filling the shape
    
    for character in state:
        color(get_random_color())  # Get a random color for each shape
        
        if character == 'F':
            fd(20)  # Forward 20 units
            delay(40)
        elif character == 'A':
            circle(20, 90)  # Draw an arc (circle(20, 90))
            delay(40)
        elif character == 'B':
            I = 20 / sqrt(2)  # Calculate forward units
            fd(I)  # Forward I units
            circle(I, 270)  # Draw an arc (circle(I, 270))
            fd(I)  # Forward I units
            delay(40)

    end_fill()  # End filling the shape
    
    # Draw the suli kolam within the outer kolam
    pu()  # Pen up to avoid drawing connections
    home()  # Return to the starting position
    pd()  # Pen down to start drawing
    color(get_random_color())  # Get a random color for the suli kolam
    draw_suli_kolam()

    return "done"

def draw_suli_kolam():
    pu()
    goto(100, -100)  # Adjust the position as per your desired location for the suli kolam
    pd()
    lt(45)
    draw_outer_kolam()
    draw_inner_kolam()

def draw_outer_kolam():
    for _ in range(4):
        fd(100)
        lt(90)

def draw_inner_kolam():
    for _ in range(4):
        fd(50)
        lt(90)

def get_random_color():
    # Generate random RGB values between 0 and 1
    r = random.random()
    g = random.random()
    b = random.random()
    
    return (r, g, b)

if __name__ == '__main__':
    msg = main()
    print(msg)
    mainloop()

