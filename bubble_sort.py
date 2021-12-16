l=[15,6,13,22,3,52,2]
print('Original list is:',l)
n=len(l)
for i in range(n):
    for j in range(n-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print('List after sorting is:',l)