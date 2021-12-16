n=int(input('Enter number:'))
lim=int(n/2)+1
for i in range(2,lim+1):
    rem=n%i
    if rem==0:
        print(n,'is not a prime number')
        break
else:
    print(n,'is a prime number')