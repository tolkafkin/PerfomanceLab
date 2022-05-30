from math import sqrt
import sys


def check(lenght, radius):
    if lenght > radius: return 2
    elif lenght < radius: return 1
    else: return 0


def calc(x_centr, y_centr, x, y):
    leg_x = round(x_centr - x, 20)
    leg_y = round(y_centr - y, 20)
    if x == x_centr:
        return abs(leg_y)    
    elif y == y_centr:
        return abs(leg_x)     
    return sqrt(round(leg_x**2, 20) + round(leg_y**2, 20))    


def main(args):
    with open(args[1], 'r') as file1:
        x_centr, y_centr = [float(element) for element in file1.readline().split()]
        rad = float(file1.readline())
    
    with open(args[2], 'r') as file2:
        for line in file2.readlines():
            x, y = [float(element) for element in line.split()]
            lenght = calc(x_centr=x_centr, y_centr=y_centr, x=x, y=y)
            print(check(lenght, rad))


if __name__ == "__main__":
    main(args=sys.argv)
