lst=eval(input('Enter a list of ten numbers:'))
ln=len(lst)
max_ele=lst[0]
max_index=0
for i in range(ln):
    if lst[i]>max_ele:
        max_ele=lst[i]
        max_index=i
print('The maximum element of list is:',max_ele,'at index',max_index)
