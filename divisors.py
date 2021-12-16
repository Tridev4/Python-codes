n=int(input('Enter an integer:'))
m=int(n/2)
print('The divisors of',n,'are:')
for a in range(2,m+1):
    if n%a==0:
        print(a,)
else:
    print('-END-')