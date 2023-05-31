from turtle import *
from math import sqrt
import random
import tkinter as tk
from PIL import Image

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

def save_animation():
    # Create a canvas to get the turtle graphics as an image
    root = tk.Tk()
    canvas = getcanvas()
    canvas.postscript(file="animation.eps", colormode='color')

    # Convert the EPS file to a high-quality PNG image
    img = Image.open("animation.eps")
    img.save("animation.png", "png", dpi=(300, 300))

    # Convert the PNG image to an MP4 video using FFmpeg
    import subprocess
    subprocess.call(['ffmpeg', '-r', '30', '-i', 'animation-%03d.png', '-vf', 'fps=30', '-c:v', 'libx264', '-crf', '18', '-preset', 'veryslow', '-pix_fmt', 'yuv420p', 'animation.mp4'])

    # Clean up the temporary files
    import os
    os.remove("animation.eps")
    os.remove("animation.png")

    return "Animation saved as 'animation.mp4'."

if __name__ == '__main__':
    msg = main()
    print(msg)
    save_animation()
    mainloop()

