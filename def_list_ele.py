def lst_ele(list1):
    x=0
    for i in range(len(list1)):
        x+=1
    return x
list1=eval(input('Enter a list:'))
print('Number of elements in the list are:',lst_ele(list1))