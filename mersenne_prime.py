for a in range(1,21):
    mn=(2**a)-1
    mid=int(mn/2)+1
    for b in range(2,mid):
        if mn%b==0:
            print(mn)
            break
    else:
        print(mn,'\tPrime')