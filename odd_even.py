#to find that a number is even or odd
#if the remainder is zero then the number is even
#if the the remainder is one then it is odd
number=int(input("Enter the number:"))
if (number % 2) == 0:
    print("The number is even")
else:
    print("The number is odd")