from turtle import *
from math import sqrt as s

def main():
    pensize(4)
    n = numinput('L system kolam', 'Enter level: ')
    lt(45)
    ht()
    s = 'FBFBFBFB'
    for _ in range(int(n)):
        f = ''
        for c in s:
            if c == 'F':
                f += c
            elif c == 'A':
                f += 'AFBFA'
            elif c == 'B':
                f += 'AFBFBFBFA'
        s = f
    
    for c in s:
        if c == 'F':
            color("green")
            fd(20)
            delay(40)
        elif c == 'A':
            color("blue")
            circle(20, 90)
            delay(40)
        elif c == 'B':
            color("red")
            i = 10 / s(2)
            fd(i)
            circle(i, 270)
            fd(i)
            delay(40)

    return "done"

if __name__ == '__main__':
    m = main()
    print(m)
    mainloop()

