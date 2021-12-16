def makenew(mystr):
    newstr=''
    c=0
    for i in mystr:
        if (c%2==0):
            newstr=newstr+str(c)
        else:
            if (i.islower()):
                newstr=newstr+i.upper()
            else:
                newstr=newstr+i
        c+=1
        newstr=newstr+i
        print('The new string is:',newstr)
makenew('sTUdeNT')