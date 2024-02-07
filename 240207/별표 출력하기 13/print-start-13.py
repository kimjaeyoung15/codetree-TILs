n=int(input())
asc_arr=range(1,n+1)
dsc_arr=range(n,0,-1)
for i in range(n):
    if i%2==1:
        for x in range(asc_arr[i//2]):print('* ',end='')
        print()
    else:
        for y in range(dsc_arr[i//2]):print('* ',end='')
        print()
for i in range(n-1,-1,-1):
    if i%2==1:
        for x in range(asc_arr[i//2]):print('* ',end='')
        print()
    else:
        for y in range(dsc_arr[i//2]):print('* ',end='')
        print()