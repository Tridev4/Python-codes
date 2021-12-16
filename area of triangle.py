side1=int(input("Enter the first side of the triangle:"))
side2=int(input("Enter the second side of the triangle:"))
side3=int(input("Enter the third side of the triangle:"))
S=side1 + side2 + side3
area=(S*(S-side1)*(S-side2)*(S-side3))**0.5
print("The area of the triangle is:",area)