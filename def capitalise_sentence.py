def capitalise_sentence():
    f1=open('test_report.txt','r')
    f2=open('file1.txt','w')
    while True:
        l=f1.readline()
        if not l:
            break
        l=l.rstrip()
        ln=len(l)
        st=''
        st+=l[0].upper()
        i=1
        while i<ln:
            if l[i]=='.':
                st+=l[i]
                if i>=ln:
                    break
                st+=l[i].upper()
            else:
                st+=l[i]
                i+=1
            f2.write(st)
        else:
            print('Source file does not exist')
        f1.close()
        f2.close()
capitalise_sentence()