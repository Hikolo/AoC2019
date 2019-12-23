from sys import argv
from math import pi, sin, cos, floor
import tkinter
import turtle

turtle.color('red', 'yellow')
_script, filename = argv

input = [x.split(',') for x in open(filename).read().split('\n')]
grid = dict()
#print(input)
wheel = {
    'R': 0,
    'U': pi/2,
    'L': pi,
    'D': (3*pi)/2
}

def addwire(wire):
    (x, y) = (0, 0)
    turtle.setpos(x, y)
    for move in wire:
        direction = wheel[move[0]]
        length = int(move[1:])
        print(f"Direction is: {direction}, length is: {length}")
        i = 0
        while i < length:
            (x, y) = (x + round(cos(direction)), y + round(sin(direction)))
            print(f"Current (x, y) is: {(x, y)}")
            if (x, y) in grid:
                grid[(x, y)] = 'X'
            else:
                grid[(x, y)] = 'O'
            i += 1
        turtle.setpos(x, y)

for wire in input:
    addwire(wire)
done()
points = [] 
for point in grid:
    if grid[point] == 'X':
        print(point)
        (x, y) = point
        points.append(abs(x) + abs(y))
print(min(points))
    
        
