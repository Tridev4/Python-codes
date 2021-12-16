import math 
print('For quadratic equation ax**2+bx+c=0, enter the coefficients')
a=int(input('Enter a:'))
b=int(input('Enter b:'))
c=int(input('Enter c:'))
if a==0:
    print('Value of a should not be zero')
    print('\n Aborting !!!!')
else:
    d=(b*b)-(4*a*c)
    if d>0:
        r1=(-b+math.sqrt(d))/(2*a)
        r2=(-b-math.sqrt(d))/(2*a)
        print('Roots are real and unequal')
        print('Root1=',r1,'Root2=',r2)
    elif d==0:
        r1=(-b)/(2*a)
        print('Roots are real and equal')
        print('Root=',r1)
    else:
        print('Roots are complex and imaginary')