# Area Calculator
# Pawelski
# 10/1/2024
# Programming Fundamentals

shape = input("What shape do you need to calculate the area for? (circle, triangle, rectangle) >> ")

if shape == "circle":
    radius = float(input("What is the radius of the circle? >> "))
    if radius >= 0:
        area = 3.14 * radius * radius
        print("area = " + str(area))
    else:
        print("Invalid radius!")
elif shape == "triangle":
    base = float(input("What is the base of the triangle? >> "))
    height = float(input("What is the height of the triangle? >> "))
    if base >= 0 and height >= 0:
        area = 0.5 * base * height
        print("area = " + str(area))
    else:
        print("Invalid base or height!")
elif shape == "rectangle":
    pass # Replace this line of code with your code!
