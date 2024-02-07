a,b=map(int,input().split())
n1=[x for x in range(b,a-1,-1)]
n2=[y for y in range(2,9,2)]
for i in n2:
    for j in n1:
        print(f'{j} * {i} = {j*i}', end='')
        if j>a:print(' / ',end='')
    print()