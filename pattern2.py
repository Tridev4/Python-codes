num=2
for i in range(5):
    for j in range(5):
        if i+j==num or j-i==num or i-j==num or i+j==5+num-1:
            print("*",end="")
        else:
            print(end=" ")
    print()