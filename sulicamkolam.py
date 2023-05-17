import cv2
import numpy as np

# L-System parameters
axiom = "FBFBFBFB"  # Initiator
rules = {
    "A": "AFFA",
    "B": "AFBFBFFA"
}
angle = 45  # Angle in degrees

# Set the dot size and number of iterations
dot_size = 20
iterations = 4

def expand_lsystem_string(axiom, rules, iterations):
    result = axiom
    for _ in range(iterations):
        result = "".join([rules.get(ch, ch) for ch in result])
    return result

# Define the L-System string
lsystem_string = expand_lsystem_string(axiom, rules, iterations)

# Function to interpret the L-System string and draw the SUZHI Kolam pattern on the frame
def draw_suzhi_kolam(lsystem_string, dot_size, frame):
    for symbol in lsystem_string:
        if symbol == "A":
            cv2.line(frame, (0, 0), (dot_size, 0), (255, 0, 0), 1)
        elif symbol == "A":
            cv2.circle(frame, (dot_size, dot_size), dot_size, (255, 0, 0), 1)
        elif symbol == "B":
            cv2.ellipse(frame, (dot_size, dot_size), (dot_size, dot_size), 0, 0, 90, (255, 0, 0), 1)

# Initialize video capture
video_capture = cv2.VideoCapture(0)

while True:
    # Read a frame from the video stream
    ret, frame = video_capture.read()

    # Draw the SUZHI Kolam pattern on the current frame
    draw_suzhi_kolam(lsystem_string, dot_size, frame)

    # Display the frame
    cv2.imshow('Live Video', frame)

    # Break the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close OpenCV windows
video_capture.release()
cv2.destroyAllWindows()
