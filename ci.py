import math
principle=float(input("Enter the principle:"))
rate=float(input("Enter the rate:"))
time=float(input("Enter the time:"))
compoundinterest=principle * (math.pow((1 + rate / 100), time))
print("Compound interest is",compoundinterest)