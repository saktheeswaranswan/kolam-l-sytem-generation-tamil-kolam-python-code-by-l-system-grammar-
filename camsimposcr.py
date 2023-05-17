import cv2
import numpy as np

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

# Expand the L-System string
def expand_lsystem_string(axiom, rules, iterations):
    result = axiom
    for _ in range(iterations):
        result = "".join([rules.get(ch, ch) for ch in result])
    return result

# Function to interpret the L-System string and draw the Suzhi Kolam pattern
def draw_suli_kolam(lsystem_string, dot_size, img):
    # Interpret the L-System string
    for symbol in lsystem_string:
        if symbol == "F+A":
            draw_line(dot_size, img)
        elif symbol == "A":
            draw_arc(dot_size, 90, img)
        elif symbol == "B":
            forward_units = 5 / (2 ** 0.5)
            draw_line(forward_units, img)
            draw_arc(forward_units, 270, img)
            cv2.circle(img, (int(x), int(y)), dot_size // 2, (0, 0, 0), -1)

# Function to draw a line segment
def draw_line(length, img):
    global x, y
    x2 = x + length * np.cos(np.radians(angle))
    y2 = y - length * np.sin(np.radians(angle))
    cv2.line(img, (int(x), int(y)), (int(x2), int(y2)), (0, 0, 0), thickness=dot_size)
    x, y = x2, y2

# Function to draw an arc
def draw_arc(radius, angle, img):
    global x, y
    x2 = x + radius * np.cos(np.radians(angle + 90))
    y2 = y - radius * np.sin(np.radians(angle + 90))
    cv2.ellipse(img, (int(x), int(y)), (int(radius), int(radius)), angle, 0, 90, (0, 0, 0), thickness=dot_size)
    x, y = x2, y2

# Initialize video capture
video_capture = cv2.VideoCapture(0)

while True:
    # Read a frame from the video stream
    ret, frame = video_capture.read()

    # Initialize the starting position for drawing the Suzhi Kolam pattern
    x, y = frame.shape[1] // 2, frame.shape[0] // 2
    angle = 0

    # Draw the Suzhi Kolam pattern on the current frame
    draw_suli_kolam(expand_lsystem_string(axiom, rules, iterations), dot_size, frame)

    # Display the frame
    cv2.imshow('Live Video', frame)

    # Break the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Resize the screen
    cv2.resize(frame, (frame.shape[1] // 2, frame.shape[0] // 2))

# Release the video capture and close OpenCV windows
video_capture.release()
cv2.destroyAllWindows()
