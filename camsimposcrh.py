import cv2
import numpy as np
import turtle

# L-System parameters
axiom = "FBFBFBFB"  # Initiator
rules = {
    "A": "AFBFA",
    "B": "AFBFBFBFA"
}
angle = 45  # Angle in degrees

# Set the dot size and number of iterations
dot_size = 10
iterations = 2

# Initialize the turtle
turtle.penup()
turtle.setposition(0, 0)

# Initialize video capture
video_capture = cv2.VideoCapture(0)

while True:
    # Read a frame from the video stream
    ret, frame = video_capture.read()

    # Draw the Suzhi Kolam pattern on the current frame
    for i in range(iterations):
        for symbol in axiom:
            if symbol == "F":
                turtle.forward(dot_size)
            elif symbol == "A":
                turtle.left(90)
                turtle.circle(dot_size, 180)
            elif symbol == "B":
                turtle.left(90)
                turtle.circle(dot_size / np.sqrt(2), 180)

    # Display the frame
    cv2.imshow('Live Video', frame)

    # Break the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close OpenCV windows
video_capture.release()
cv2.destroyAllWindows()
