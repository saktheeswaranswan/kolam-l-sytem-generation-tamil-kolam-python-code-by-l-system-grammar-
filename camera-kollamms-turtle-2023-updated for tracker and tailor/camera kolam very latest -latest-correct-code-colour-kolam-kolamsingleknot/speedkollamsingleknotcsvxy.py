import csv
from turtle import *
from math import sqrt


def main():
    step_size = 20
    coordinates = []

    pensize(4)
    n = numinput('L system kolam', 'Enter level: ')
    lt(45)
    ht()
    state = 'FBFBFBFB'

    for _ in range(int(n)):
        final_state = ''
        for character in state:
            if character == 'F':
                final_state += character
            elif character == 'A':
                final_state += 'AFBFA'
            elif character == 'B':
                final_state += 'AFBFBFBFA'
        state = final_state

    speed(0)

    for character in state:
        if len(coordinates) >= 10000:
            break

        if character == 'F':
            color("green")
            fd(step_size)
            current_pos = (xcor(), ycor())
            coordinates.append(current_pos)

            while abs(xcor() - current_pos[0]) >= step_size or abs(ycor() - current_pos[1]) >= step_size:
                fd(step_size)
                current_pos = (xcor(), ycor())
                coordinates.append(current_pos)

            delay(40)
        elif character == 'A':
            color("blue")
            circle(20, 90)
            current_pos = (xcor(), ycor())
            coordinates.append(current_pos)

            while abs(xcor() - current_pos[0]) >= step_size or abs(ycor() - current_pos[1]) >= step_size:
                fd(step_size)
                current_pos = (xcor(), ycor())
                coordinates.append(current_pos)

            delay(40)
        elif character == 'B':
            color("red")
            I = 10 / sqrt(2)
            fd(I)
            current_pos = (xcor(), ycor())
            coordinates.append(current_pos)

            while abs(xcor() - current_pos[0]) >= step_size or abs(ycor() - current_pos[1]) >= step_size:
                fd(step_size)
                current_pos = (xcor(), ycor())
                coordinates.append(current_pos)

            circle(I, 270)
            fd(I)
            current_pos = (xcor(), ycor())
            coordinates.append(current_pos)

            while abs(xcor() - current_pos[0]) >= step_size or abs(ycor() - current_pos[1]) >= step_size:
                fd(step_size)
                current_pos = (xcor(), ycor())
                coordinates.append(current_pos)

            delay(40)

    with open('coordinates.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['x', 'y'])
        writer.writerows(coordinates)

    return "done"


if __name__ == '__main__':
    msg = main()
    print(msg)
    mainloop()

