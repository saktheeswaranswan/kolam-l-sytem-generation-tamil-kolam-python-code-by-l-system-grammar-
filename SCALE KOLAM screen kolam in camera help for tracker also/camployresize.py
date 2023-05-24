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

# Define output video file parameters
output_file = 'output.mp4'
output_fps = 30.0  # Frames per second
output_size = (1280, 720)  # Output video size

# Define the codec for video writing
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_file, fourcc, output_fps, output_size)

while True:
    # Read frame from video stream
    ret, frame = cap.read()
    if not ret:
        break
    
    # Get current X, Y coordinates from the CSV data
    for x, y in data.values:
        # Draw big red circle at the specified coordinates
        cv2.circle(frame, (x, y), circle_radius, circle_color, circle_thickness)

    # Resize the screen
    frame = cv2.resize(frame, output_size)

    # Write the frame to the output video file
    out.write(frame)

    # Show the frame
    cv2.imshow('Video Stream', frame)
    
    # Wait for key press
    key = cv2.waitKey(1) & 0xFF
    
    # Check if 'n' key is pressed to move the point
    if key == ord('n'):
        # Increase current row index
        current_row += 1
        
        # Reset current row index if it exceeds the number of rows in the CSV file
        if current_row >= len(data):
            current_row = 0

    # Break the loop if 'q' key is pressed
    if key == ord('q'):
        break

# Release video capture and close windows
cap.release()
out.release()
cv2.destroyAllWindows()

