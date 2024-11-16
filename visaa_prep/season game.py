n=int(input())
l=[[3,4,5],[6,7,8],[9,10,11],[12,1,2]]
if n in l[0]:
    print("Spring")
elif n in l[1]:
    print("Summer")
elif n in l[2]:
    print("Autumn")
elif n in l[3]:
    print("Winter")
else:
    print("Invalid")
