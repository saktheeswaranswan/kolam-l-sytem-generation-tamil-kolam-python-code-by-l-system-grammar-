import turtle
import numpy as np

def create_polygon(center, sides, radius):
    angle = 2 * np.pi / sides
    points = []
    for i in range(sides):
        x = center[0] + radius * np.cos(i * angle)
        y = center[1] + radius * np.sin(i * angle)
        points.append((x, y))
    return points

def draw_polygon(polygon):
    turtle.penup()
    turtle.goto(polygon[0])
    turtle.pendown()
    for point in polygon[1:]:
        turtle.goto(point)
    turtle.goto(polygon[0])

def create_rangoli(grid_size, polygon1, polygon2):
    center = (0, 0)
    turtle.speed(0)
    turtle.bgcolor('white')

    for i in range(grid_size-1, -1, -1):
        turtle.penup()
        turtle.goto(0, i * 40)
        turtle.pendown()

        for j in range(0, i):
            turtle.write('--', align='center', font=('Arial', 12, 'normal'))

        for j in range(grid_size-1, i, -1):
            polygon = polygon1 if (j % 2 == 0) else polygon2
            scaled_polygon = [(point[0]*40, point[1]*40) for point in polygon]
            translated_polygon = [(point[0] + (j-i)*40, point[1] + i*40) for point in scaled_polygon]
            draw_polygon(translated_polygon)
        
        for j in range(i, grid_size):
            polygon = polygon1 if (j % 2 == 0) else polygon2
            scaled_polygon = [(point[0]*40, point[1]*40) for point in polygon]
            translated_polygon = [(point[0] + (j-i)*40, point[1] + i*40) for point in scaled_polygon]
            draw_polygon(translated_polygon)
        
        turtle.goto(grid_size*40-40, i * 40)
        for j in range(0, 2*i - 1):
            turtle.write('-', align='center', font=('Arial', 12, 'normal'))
        turtle.write('-', align='center', font=('Arial', 12, 'normal'))
        turtle.write('\n')

    for i in range(1, grid_size):
        turtle.penup()
        turtle.goto(0, i * 40)
        turtle.pendown()

        for j in range(0, i):
            turtle.write('--', align='center', font=('Arial', 12, 'normal'))

        for j in range(grid_size-1, i, -1):
            polygon = polygon1 if (j % 2 == 0) else polygon2
            scaled_polygon = [(point[0]*40, point[1]*40) for point in polygon]
            translated_polygon = [(point[0] + (j-i)*40, point[1] + i*40) for point in scaled_polygon]
            draw_polygon(translated_polygon)
        
        for j in range(i, grid_size):
            polygon = polygon1 if (j % 2 == 0) else polygon2
            scaled_polygon = [(point[0]*40, point[1]*40) for point in polygon]
            translated_polygon = [(point[0] + (j-i)*40, point[1] + i*40) for point in scaled_polygon]
            draw_polygon(translated_polygon)
        
        turtle.goto(grid_size*40-40, i * 40)
        for j in range(0, 2*i - 1):
            turtle.write('-', align='center', font=('Arial', 12, 'normal'))
        turtle.write('-', align='center', font=('Arial', 12, 'normal'))
        turtle.write('\n')

    turtle.hideturtle()
    turtle.done()

# Define the parameters for the polygons
polygon1_center = (0, 0)
polygon1_sides = 6
polygon1_radius = 3

polygon2_center = (0, 0)
polygon2_sides = 8
polygon2_radius = 2

# Create the rangoli
create_rangoli(8, create_polygon(polygon1_center, polygon1_sides, polygon1_radius),
               create_polygon(polygon2_center, polygon2_sides, polygon2_radius))

