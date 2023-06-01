from turtle import *
from math import sqrt
import random
import cv2
import numpy as np

# Webcam settings
WIDTH, HEIGHT = 640, 480  # Width and height of the video frame

def main():
    pensize(2)
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
    
    # Select background canvas
    bg_canvas = numinput('L system kolam', 'Select background canvas (0: Black, 1: White, 2: Webcam): ')
    
    if bg_canvas == 2:
        setup_webcam(n)
    else:
        bgcolor('black' if bg_canvas == 0 else 'white')

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

def setup_webcam(n):
    cv2.namedWindow("Webcam")
    cap = cv2.VideoCapture(0)
    cap.set(3, WIDTH)
    cap.set(4, HEIGHT)
    while True:
        _, frame = cap.read()
        cv2.imshow("Webcam", frame)
        
        # Convert BGR frame to RGB for turtle graphics
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Create an image from the RGB frame
        img = np.array(frame_rgb)
        draw = cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2BGR)
        
        # Call the turtle kolam plotting function on the image
        plot_turtle_kolam(draw, n)
        
        cv2.imshow("Webcam with Kolam", draw)
        
        if cv2.waitKey(1) == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

def plot_turtle_kolam(draw, n):
    # Set the turtle's starting position
    x, y = 0, 0
    
    # Set the turtle's heading angle
    angle = 45
    
    # Set the turtle's step size
    step = 20
    
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
    
    for character in state:
        color = get_random_color()  # Get a random color for each shape
        
        if character == 'F':
            cv2.line(draw, (int(x), int(y)), (int(x + step), int(y)), color, thickness=2)
            x += step
        elif character == 'A':
            radius = step / 2
            cv2.ellipse(draw, (int(x + radius), int(y - radius)), (int(radius), int(radius)), 0, 0, 90, color, thickness=2)
            x += radius * 2
        elif character == 'B':
            i = step / sqrt(2)
            cv2.line(draw, (int(x), int(y)), (int(x + i), int(y + i)), color, thickness=2)
            cv2.ellipse(draw, (int(x + i), int(y + i - step)), (int(i), int(step)), 270, 0, 360, color, thickness=2)

if __name__ == '__main__':
    msg = main()
    print(msg)
    mainloop()

