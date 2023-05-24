import csv
import cv2

def extract_coordinates(image_path, color):
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Set the color threshold based on user input
    if color == 'white':
        threshold = 255
    elif color == 'black':
        threshold = 0
    else:
        print("Invalid color choice. Please choose 'white' or 'black'.")
        return
    
    # Extract the coordinates
    points = []
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            if image[y, x] == threshold:
                points.append((x, y))
                if len(points) >= 100000:
                    return points
    
    return points

def export_to_csv(points, output_path):
    with open(output_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['X', 'Y'])
        writer.writerows(points)

# Example usage
image_path = '/home/josva/kollamms turtle/kolamsingleknot/binary_image.png'
color_choice = input("Enter color choice (white/black): ")
output_path = 'output.csv'

points = extract_coordinates(image_path, color_choice)
export_to_csv(points, output_path)

print(f"Extracted {len(points)} coordinates and exported to '{output_path}'.")

