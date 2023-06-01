from turtle import *
from math import sqrt
import random

def main():
    pensize(10)
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
    
    begin_fill()  # Begin filling the shape
    
    for character in state:
        color(get_random_color())  # Get a random color for each shape
        
        if character == 'F':
            fd(20)  # Forward 10 units
            delay(40)
        elif character == 'A':
            circle(20, 90)  # Draw an arc (circle(10, 90))
            delay(40)
        elif character == 'B':
            I = 10 / sqrt(2)  # Calculate forward units
            fd(I)  # Forward I units
            circle(I, 270)  # Draw an arc (circle(I, 270))
            fd(I)  # Forward I units
            delay(40)

    end_fill()  # End filling the shape
    
    return "done"

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

