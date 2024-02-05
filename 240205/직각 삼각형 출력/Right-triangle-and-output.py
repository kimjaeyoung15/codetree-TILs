n=int(input())
for i in range(1,n+1):
    arr=['*' for _ in range(2*i-1)]
    print(*arr, sep='')