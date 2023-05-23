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

while True:
    # Read frame from video stream
    ret, frame = cap.read()
    if not ret:
        break
    
    # Get current X, Y coordinates from the CSV data
    x = data.iloc[current_row]['X']
    y = data.iloc[current_row]['Y']
    
    # Draw big red circle at the specified coordinates
    cv2.circle(frame, (x, y), circle_radius, circle_color, circle_thickness)
    
    # Show the frame
    cv2.imshow('Video Stream', frame)
    
    # Wait for key press
    key = cv2.waitKey(1) & 0xFF
    
    # Check if 'n' key is pressed to blink the next row
    if key == ord('n'):
        # Increase current row index
        current_row += 1
        
        # Reset current row index if it exceeds the number of rows in the CSV file
        if current_row >= len(data):
            current_row = 0
        
        # Blink the red circle by toggling its visibility
        circle_color = (0, 0, 255) if circle_color == (0, 0, 0) else (0, 0, 0)  # Toggle between black and red
    
    # Break the loop if 'q' key is pressed
    if key == ord('q'):
        break

# Release video capture and close windows
cap.release()
cv2.destroyAllWindows()

