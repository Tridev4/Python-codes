lst=eval(input('Enter the list of marks:'))
t=int(input('Enter maximum marks:'))
s=0
ln=len(lst)
for i in range(ln):
    s+=lst[i]
p=(s/t)*100
print('Total marks obtained are:',s)
print('Percentage is:',p)