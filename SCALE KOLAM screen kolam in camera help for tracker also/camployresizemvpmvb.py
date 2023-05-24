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

    # Plot all points as small red circles
    for point in data.values:
        cv2.circle(frame, (int(point[0]), int(point[1])), circle_radius, (0, 0, 255), -1)

    # Draw thick blue circle for the moving point
    cv2.circle(frame, (int(start_point[0]), int(start_point[1])), circle_radius + 5, (255, 0, 0), circle_thickness)

    # Show the frame
    cv2.imshow('Video Stream', frame)
    
    # Wait for key press
    key = cv2.waitKey(1) & 0xFF
    
    # Check if 'n' key is pressed to move the point
    if key == ord('n'):
        current_row += 1
        if current_row >= len(data):
            current_row = 0

        move_count = 0
        start_point = None
        end_point = None

    # Break the loop if 'q' key is pressed
    if key == ord('q'):
        break

# Release video capture and close windows
cap.release()
cv2.destroyAllWindows()

