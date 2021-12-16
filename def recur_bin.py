def bin_sr(l,low,h,v):
    if h<low:
        return None
    else:
        mv=low+((h-low)//2)
        if l[mv]>v:
            return bin_sr(l,low,mv-1,v)
        elif l[mv]<v:
            return bin_sr(l,mv+1,h,v)
        else:
            return mv
l=[5,11,22,36,99,101]
print(bin_sr(l,0,5,36))
print(bin_sr(l,0,5,100))