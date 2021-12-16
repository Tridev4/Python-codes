no=int(input("Enter the number:"))
newn=0
dgt=0
temp=no
while no:
    dgt=no%10
    newn=newn*10+dgt
    no=no//10
if newn==temp:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")