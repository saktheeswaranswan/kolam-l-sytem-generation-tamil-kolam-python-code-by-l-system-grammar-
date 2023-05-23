import cv2
import numpy as np

# Load the video file
cap = cv2.VideoCapture("video.mp4")

# Load the transparent PNG image
png = cv2.imread("transparent.png")

# Create a mask for the transparent PNG image
if png is not None:
    mask = np.zeros(png.shape[:2], dtype="uint8")
    mask[png[:, :, 2] == 255] = 255

# Create a background subtractor
bg_subtractor = cv2.createBackgroundSubtractorMOG2()

while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # Apply the background subtractor to the frame
    if ret == True:
        fg_mask = bg_subtractor.apply(frame)

    # Combine the foreground mask and the transparent PNG image
    combined_mask = np.bitwise_and(fg_mask, mask)

    # Apply the combined mask to the frame
    frame = cv2.bitwise_and(frame, frame, mask=combined_mask)

    # Display the frame
    cv2.imshow("Live Stream", frame)

    # Wait for a key press
    key = cv2.waitKey(1)

    # If the key `q` is pressed, stop the loop
    if key == ord("q"):
        break

# Release the video capture object
cap.release()

# Destroy all windows
cv2.destroyAllWindows()

