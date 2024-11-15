X,Y=map(int,input().split())
m=0
while X>=Y:
    X -=Y
    m +=1
print(m)
