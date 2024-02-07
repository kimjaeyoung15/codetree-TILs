n=int(input())
p=9
for i in range(n):
    for j in range(n):
        if p!=1:
            print(p,end='')
            p-=1
        else:
            print(p,end='')
            p=9
    print()