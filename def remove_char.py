def remove_char(st,n):
    f=st[:n]
    l=st[n+1:]
    return f+l
st=input('Enter a string:')
n=int(input('Enter a number:'))
print(remove_char(st,n))