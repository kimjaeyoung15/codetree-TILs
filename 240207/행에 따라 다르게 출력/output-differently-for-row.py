n=int(input())
s=0
row=1
for i in range(n):
    if row%2==1:
        for j in range(n):
            s+=1
            print(s,end=' ')
    if row%2==0:
        for j in range(n):
            s+=2
            print(s,end=' ')
    print()
    row+=1