def recur_gcd(p,q):
    if q==0:
        return p
    else:
        return recur_gcd(q,p%q)
p=int(input('Enter first number:'))
q=int(input('Enter second number:'))
print('Greatest common divisor is:',recur_gcd(p,q))
