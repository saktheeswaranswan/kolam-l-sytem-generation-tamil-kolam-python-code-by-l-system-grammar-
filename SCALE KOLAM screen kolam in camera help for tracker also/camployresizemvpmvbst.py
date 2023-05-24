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
circle_thickness = -1  # Filled circle
circle_color = (0, 0, 255)  # Red color (BGR format)

# Initialize current row index
current_row = 0

# Get start and end points
start_point = tuple(data.values[0])
end_point = tuple(data.values[-1])

# Calculate the step size for moving from start to end
step_x = (end_point[0] - start_point[0]) / len(data)
step_y = (end_point[1] - start_point[1]) / len(data)

while True:
    # Read frame from video stream
    ret, frame = cap.read()
    if not ret:
        break

    # Plot all points as small red circles
    for point in data.values:
        cv2.circle(frame, (int(point[0]), int(point[1])), circle_radius, (0, 0, 255), -1)

    # Calculate the current position of the moving point
    current_x = int(start_point[0] + current_row * step_x)
    current_y = int(start_point[1] + current_row * step_y)

    # Draw thick blue circle for the moving point
    cv2.circle(frame, (current_x, current_y), circle_radius + 5, (255, 0, 0), circle_thickness)

    # Show the frame
    cv2.imshow('Video Stream', frame)

    # Increment the current row index
    current_row += 1

    # Break the loop if all points have been traversed
    if current_row >= len(data):
        break

    # Wait for key press
    key = cv2.waitKey(1) & 0xFF

    # Break the loop if 'q' key is pressed
    if key == ord('q'):
        break

# Release video capture and close windows
cap.release()
cv2.destroyAllWindows()

