l=eval(input('Enter a list:'))
x=int(input("Enter a number:"))
found=False
for i in range(len(l)):
    if (l[i]==x):
        found=True
        print("%d found at %dth position"%(x,i))
        print(l)
        break
    if (found==False):
        print("%d is not in the list"%x)