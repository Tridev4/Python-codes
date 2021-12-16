lst=eval(input('Enter a list of ten numbers:'))
ln=len(lst)
min_ele=lst[0]
min_index=0
for i in range(ln):
    if lst[i]<min_ele:
        min_ele=lst[i]
        min_index=i
print('The minimum element of list is:',min_ele,'at index',min_index)
