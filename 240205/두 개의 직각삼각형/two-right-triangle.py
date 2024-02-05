n=int(input())
for i in range(n,0,-1):
    for x in range(i):
        print('*',end='')
    for y in range((n-i)*2):
        print(' ',end='')
    for z in range(i):
        print('*',end='')
    print()