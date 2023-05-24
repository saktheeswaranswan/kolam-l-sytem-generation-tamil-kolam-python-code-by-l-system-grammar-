import cv2
import numpy as np
import csv

def convert_image_to_binary(image_path):
    # Read the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Convert the image to binary
    _, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

    return binary_image

def export_coordinates(binary_image, output_csv, max_points=10000):
    # Find white pixel coordinates
    white_pixels = np.where(binary_image == 255)

    # Limit the number of points to export
    if len(white_pixels[0]) > max_points:
        indices = np.random.choice(len(white_pixels[0]), max_points, replace=False)
        white_pixels = (white_pixels[0][indices], white_pixels[1][indices])

    # Write coordinates to CSV
    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['x', 'y'])
        for x, y in zip(white_pixels[1], white_pixels[0]):
            writer.writerow([x, y])

# Path to input image
image_path = '/home/josva/kollamms turtle/correct-code-colour-kolam-kolamsingleknot/binary_image.png'

# Path to output CSV file
output_csv = 'output_coordinates.csv'

# Convert image to binary
binary_image = convert_image_to_binary(image_path)

# Export coordinates to CSV
export_coordinates(binary_image, output_csv)

