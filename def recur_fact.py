def recur_fact(n):
    if n==1:
        return n
    else:
        return n*recur_fact(n-1)
n=int(input('Enter a number:'))
if n<0:
    print('Factorial of negative number does not exist.')
elif n==0:
    print('The factorial of 0 is 1.')
else:
    print('The factorial of',n,'is:',recur_fact(n))