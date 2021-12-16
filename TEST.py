def sum_n(n):
    s=0
    for i in str(n):
        s+=int(i)
    return s
x=int(input("Enter the total quantity of numbers:"))
for i in range(1,x+1):
    n=input("Enter the number:")
    print("Sum of digits of the number is:",sum_n(n))