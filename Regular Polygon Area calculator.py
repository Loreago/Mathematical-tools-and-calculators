from math import tan, pi
print("Hello!")
print("This is a program that calculates The area and other aspects of your polygon.")
number_of_sides=int(input("How many sides does your Polgyon have? "))
side_length=int(input("What is the length of each side? "))
Area= number_of_sides*((side_length**2)/(4*tan(pi/number_of_sides)))
Perimeter= number_of_sides*side_length
interior_angle= ((number_of_sides-2)*180)
exterior_angle= 360/number_of_sides

print(f"The Area of your Polygon is {Area} and its Perimeter is {Perimeter}.")
print(f"It is a Polygon and its Interior angle is {interior_angle/number_of_sides} degrees. The sum of its interior angles is {interior_angle} degrees. Its Exterior angle is {exterior_angle} degrees")

