lst=eval(input('Enter the list of numbers:'))
s=t=0
for i in lst:
    s+=i
    t+=1
av=s/t
print('Average is:',av)