#=============================
# Auther : Rujira Navaen
# ID 1660700384
# Section 127E
# Date 14 Jan 2024
# Lab Number 1
#=============================

import math
def display_menu():
    # Display the main menu with shape code options.
    print("==========================================")
    print("|     *** Area Calculator Program ***    |")
    print("------------------------------------------")
    print("| Shape code list:                       |")
    print("|      (R) Rectangle                     |")
    print("|      (T) Trapezoid                     |")
    print("|      (C) Circle                        |")
    print("------------------------------------------")

def calculate_rectangle_area(width, height):
    # Calculate and return the area of a rectangle.
    return width * height

def rectangle():
    # Input for width and height
    print("=======================================")
    width = float(input("Enter width: "))
    height = float(input("Enter height: "))
    
    # Calculate the area
    area = calculate_rectangle_area(width, height)
    # Display the result
    print("=======================================")
    print(f"|    Area of Rectangle: {area:.2f}    |")
    print("=======================================")
    print()

def calculate_trapezoid_area(base1, base2, height):
    # Calculate and return the area of a trapezoid.
    return 0.5 * (base1 + base2) * height

def trapezoid():
    # Input for base1, base2, and height
    print("=======================================")
    base1 = float(input("Enter base1: "))
    base2 = float(input("Enter base2: "))
    height = float(input("Enter height: "))
    
    # Calculate the area
    area = calculate_trapezoid_area(base1, base2, height)
    
    # Display the result
    print("=======================================")
    print(f"|     Area of Trapezoid: {area:.2f}   |")
    print("=======================================")
    print()

def calculate_circle_area(radius):
    # Calculate and return the area of a circle.
    return math.pi * radius**2

def circle():
    # Input for the radius
    
    radius = float(input("Enter radius: "))
    
    # Calculate the area
    area = calculate_circle_area(radius)
    
    # Display the result
    print("=======================================")
    print(f"|     Area of Circle: {area:.2f}     |")
    print("=======================================")

def main():
    # Main function to run the Area Calculator Program.
    while True:
        display_menu()
        choice = input("Select Code [R, T, C]: ").upper()

        if choice == 'R':
            print('You selected R = Rectangle')
            rectangle()
        elif choice == 'T':
            print('You selected T = Trapezoid')
            trapezoid()
        elif choice == 'C':
            print('You selected C = Circle')
            circle()
        else:
            print("You select %s = Invalid shape code!"%choice)
            print('Please try again.')
            break  # Exit the program for invalid choices
if __name__ == "__main__":
    main()
