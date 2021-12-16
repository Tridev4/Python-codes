def file_long(f):
    lt=''
    for l in open(f):
        if len(l)>len(lt):
            lt=l
    print('Longest line is:',lt,'of length:',len(lt))
file_long()