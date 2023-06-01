import cv2
import matplotlib.pyplot as plt
import matplotlib.tri as tri
import matplotlib.transforms as transforms
import numpy as np
import time

def draw_rangoli(frame):
    n_angles = 36
    n_radii = 8
    min_radius = 0.25
    radii = np.linspace(min_radius, 0.95, n_radii)

    angles = np.linspace(0, 2 * np.pi, n_angles, endpoint=False)
    angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
    angles[:, 1::2] += np.pi / n_angles

    x = (radii * np.cos(angles)).flatten()
    y = (radii * np.sin(angles)).flatten()

    triang = tri.Triangulation(x, y)

    triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                             y[triang.triangles].mean(axis=1))
                    < min_radius)

    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.triplot(triang, 'b-', lw=1)
    ax.set_title('Symmetry-Preserving Rangoli')
    ax.axis(False)

    # Plotting symmetry-preserving rangoli
    ax.triplot(triang, 'b-', lw=1)
    
    # Apply rotation transformation for symmetry
    rotation = transforms.Affine2D().rotate_deg(120)
    ax.triplot(triang, 'r-', lw=1, transform=rotation + ax.transData)

    rotation = transforms.Affine2D().rotate_deg(240)
    ax.triplot(triang, 'g-', lw=1, transform=rotation + ax.transData)

    # Convert the plot to an image
    fig.canvas.draw()
    img = np.array(fig.canvas.renderer.buffer_rgba())

    # Resize the image to match the webcam frame size
    img = cv2.resize(img, (frame.shape[1], frame.shape[0]))

    # Merge the plot image with the webcam frame
    result = cv2.addWeighted(frame, 0.7, img, 0.3, 0)

    # Display the result
    cv2.imshow('Rangoli', result)
    cv2.waitKey(1)

# Open the webcam
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    if not ret:
        break

    # Draw the rangoli on the frame
    draw_rangoli(frame)

    # Wait for 0.5 seconds
    time.sleep(0.5)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()

