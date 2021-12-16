def fact(num):
    r=1
    while num>=1:
        r*=num
        num-=1
    return r
for i in range(1,5):
    print('The factorial of',i,'is:',fact(i))