import cv2
import numpy as np
import pandas as pd

# Load CSV data
csv_file = 'output.csv'  # Path to your CSV file
data = pd.read_csv(csv_file)

# Initialize video capture
cap = cv2.VideoCapture(0)  # Change to the appropriate video source if needed

# Initialize circle parameters
circle_radius = 10
circle_thickness = 2
circle_color = (0, 0, 255)  # Red color (BGR format)

# Initialize current row index
current_row = 0

# Initialize blinking variables
blink_interval = 10  # Number of frames for each blink
blink_count = 0
blink_on = True

# Initialize moving variables
move_frames = 30  # Number of frames to move from one point to another
move_count = 0
start_point = None
end_point = None
delta_x = 0
delta_y = 0

while True:
    # Read frame from video stream
    ret, frame = cap.read()
    if not ret:
        break
    
    # Get current X, Y coordinates from the CSV data
    x, y = data.values[current_row]

    if start_point is None:
        start_point = (x, y)
        end_point = (x, y)
        move_count = move_frames
    else:
        if move_count >= move_frames:
            move_count = 0
            start_point = end_point
            current_row += 1
            if current_row >= len(data):
                current_row = 0
            end_point = tuple(data.values[current_row])
            delta_x = (end_point[0] - start_point[0]) / move_frames
            delta_y = (end_point[1] - start_point[1]) / move_frames
        else:
            move_count += 1
            start_point = (start_point[0] + delta_x, start_point[1] + delta_y)

    # Blinking effect
    if blink_count < blink_interval:
        blink_on = True
    elif blink_count < blink_interval * 2:
        blink_on = False
    else:
        blink_count = 0

    # Draw circle at the specified coordinates if blinking is on
    if blink_on:
        cv2.circle(frame, (int(start_point[0]), int(start_point[1])), circle_radius, circle_color, circle_thickness)

    # Show the frame
    cv2.imshow('Video Stream', frame)
    
    # Wait for key press
    key = cv2.waitKey(1) & 0xFF
    
    # Check if 'n' key is pressed to move the point
    if key == ord('n'):
        current_row += 1
        if current_row >= len(data):
            current_row = 0

        blink_count = 0
        move_count = 0
        start_point = None
        end_point = None

    # Break the loop if 'q' key is pressed
    if key == ord('q'):
        break

    # Increment blink count
    blink_count += 1

# Release video capture and close windows
cap.release()
cv2.destroyAllWindows()

