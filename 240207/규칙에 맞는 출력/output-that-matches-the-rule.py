n=int(input())
arr=[int(x) for x in range(1,n+1)]
for i in range(n-1,-1,-1):
    print(*arr[i:],sep=' ')