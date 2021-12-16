def average(lst):
    s=t=0
    for i in lst:
        s+=i
        t+=1
        av=s/t
    return av
lst=eval(input('Enter the list of numbers:'))
print('Average is:',average(lst))