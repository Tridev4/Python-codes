l1=eval(input('Enter first list:'))
l2=eval(input('Enter second list:'))
l3=[]
if len(l1)!=len(l2):
    print('Enter same size list!!!!')
else:
    for i in range(len(l1)):
        l3.append(l1[i]+l2[i])
print('Third list is:',l3)