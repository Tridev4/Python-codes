def char_frequency(st):
    d={}
    for n in st:
        k=d.keys()
        if n in k:
            d[n]+=1
        else:
            d[n]=1
    return d
st=input('Enter a string:')
print(char_frequency(st))