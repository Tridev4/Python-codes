lst=eval(input("Enter a list:"))
fact=1
a=1
for i in lst:
    while a<=i:
        fact*=a
        a+=1
    print("Factorial of",i,'is',fact)