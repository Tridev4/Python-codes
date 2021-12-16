#to check whether a person is older between two people
#two ages will be taken as input
x=int(input("Age of first person:",))
y=int(input("Age of second person:",))
if x>y:
    print("First person is elder")
if x<y:
    print("Second person is elder")
if x==y:
    print("Both persons are of same age")