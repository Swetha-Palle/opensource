V,C=list(map(str,input().split()))
l=['R','P','S']
if(V,C in l):
    if ((V=='R' and C =='P') or (V=='P' and C=='S') or (V=='S' and C=='R')):
        print("Charan")
    elif (V==C):
        print("NULL")
    else:
        print("Vignesh")
else:
    print("NULL") 
