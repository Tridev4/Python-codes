def min_element(lst):
    ln=len(lst)
    min_ele=lst[0]
    min_index=0
    for i in range(ln):
        if lst[i]<min_ele:
            min_ele=lst[i]
            min_index=i
    return min_ele,min_index
lst=eval(input('Enter a list of numbers:'))
print('Minimum element and at index is:',min_element(lst))