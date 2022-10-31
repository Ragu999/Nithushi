l=[]
n=list(map(eval,input().split()))
x=len(n)
while n!=[-1]:
    l.append(n)
    n=list(map(eval,input().split()))
for i in range(len(l)):
    if len(l[i])!=x:
        print("Invalid Matrix")
        break
else:
    for i in range(len(l[0])):
        for j in range(len(l)):
            print(l[j][i],end=' ')
        print()
    
    
