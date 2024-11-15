A,B,C,x = list(map(int,input().split()))
if (A+B>=x or B+C>=x or C+A>=x):
    print("YES")
else:
    print("NO")
