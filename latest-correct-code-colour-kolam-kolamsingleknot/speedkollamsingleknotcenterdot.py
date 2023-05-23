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
    
    for character in state:
        if character == 'F':
            color("green")
            fd(20)  # Forward 10 units
            delay(40)
            color("black")  # Switch color to black
            dot(10)  # Draw a black dot at the geometric center of the green knot
            bk(20)  # Move back to the starting position of the knot
        elif character == 'A':
            color("blue")
            circle(20, 90)  # Draw an arc (circle(10, 90))
            delay(40)
            color("black")  # Switch color to black
            dot(10)  # Draw a black dot at the geometric center of the blue knot
            circle(-20, 90)  # Move back to the starting position of the knot
        elif character == 'B':
            color("red")
            I = 10 / sqrt(2)  # Calculate forward units
            fd(I)  # Forward I units
            color("black")  # Switch color to black
            dot(10)  # Draw a black dot at the geometric center of the red knot
            circle(-I, 90)  # Move back to the starting position of the knot
            fd(-I)  # Move back to the starting position of the knot
            circle(I, 270)  # Draw an arc (circle(I, 270))
            fd(I)  # Forward I units
            delay(40)

    return "done"

if __name__ == '__main__':
    msg = main()
    print(msg)
    mainloop()

