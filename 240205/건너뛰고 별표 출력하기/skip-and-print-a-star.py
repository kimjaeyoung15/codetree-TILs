n=int(input())
i=1
while i>0 and i<=n:
    for x in range(i):print('*',end='')
    print('\n')
    i+=1
i-=2
while i>0:
    for y in range(i):print('*',end='')
    print('\n')
    i-=1