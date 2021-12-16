for i in range(4):
    for j in range(3-i):
        print(end=" ")
    for k in range(i):
        print("*",end=" ")
    print()
for i in range(2,0,-1):
    for j in range(3-i):
        print(end=" ")
    for k in range(i):
        print("*",end=" ")
    print()