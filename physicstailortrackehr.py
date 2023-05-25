import cv2
import numpy as np
import pandas as pd

# Load CSV data
csv_file = 'output.csv'  # Path to your CSV file
data = pd.read_csv(csv_file)

# Calculate the farthest points in x and y directions
max_x = data['x'].max()
min_x = data['x'].min()
max_y = data['y'].max()
min_y = data['y'].min()

# Calculate the width and height based on the farthest points
width = int(max_x - min_x) + 100  # Add some padding
height = int(max_y - min_y) + 100  # Add some padding

# Initialize video capture
cap = cv2.VideoCapture(0)  # Change to the appropriate video source if needed

# Video dimensions and frame rate
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
fps = 30.0

# Initialize video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, fps, (width, height))

# Initialize circle parameters
circle_radius = 10
circle_thickness = -1  # Filled circle
circle_color = (0, 0, 255)  # Red color (BGR format)

# Initialize current row index and movement speed
current_row = 0
movement_speed = 100  # Default speed (can be adjusted by the user)

# ...

while True:
    # Read frame from video stream
    ret, frame = cap.read()
    if not ret:
        break

    # Plot all points as small red circles
    for point in data.values:
        x = int(point[0]) - min_x + 50  # Adjust x-coordinate based on the minimum x value and padding
        y = int(point[1]) - min_y + 50  # Adjust y-coordinate based on the minimum y value and padding
        cv2.circle(frame, (x, y), circle_radius, (0, 0, 255), -1)

    # Calculate the current position of the moving point
    current_x = int(data.values[current_row][0]) - min_x + 50
    current_y = int(data.values[current_row][1]) - min_y + 50

    # Draw thick blue circle for the moving point
    cv2.circle(frame, (current_x, current_y), circle_radius + 5, (255, 0, 0), circle_thickness)

    # Show the frame
    cv2.imshow('Video Stream', frame)

    # Write the frame to the output video file
    out.write(frame)

    # Increment the current row index based on the movement speed
    current_row += movement_speed

    # Wrap around to the start or end of the CSV data if the index goes beyond the range
    if current_row >= len(data):
        current_row = 0
    elif current_row < 0:
        current_row = len(data) - 1

    # Wait for key press
    key = cv2.waitKey(1) & 0xFF

    # Adjust the movement speed based on user input
    if key == ord('f'):
        movement_speed *= 2  # Double the movement speed
    elif key == ord('s'):
        movement_speed //= 2  # Halve the movement speed

    # Break the loop if 'q' key is pressed
    if key == ord('q'):
        break

# Release video capture and close windows
cap.release()
out.release()
cv2.destroyAllWindows()

    #
