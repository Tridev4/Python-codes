def recur_mult(n,t):
    if n==1:
        return t
    else:
        return recur_mult(n-1,t)+t
t=int(input('Enter the number:'))
for i in range(1,5):
    print(recur_mult(i,t),end=' ')