n=int(input())
for i in range(1,n+1):
    for x in range(1,n-i+2):
        print(f'{i} * {x} = {i*x}',end='')
        if x<n-i+1:print(' / ',end='')
    print()