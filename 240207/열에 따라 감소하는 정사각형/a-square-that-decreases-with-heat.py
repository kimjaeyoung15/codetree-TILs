n=int(input())
arr=list(range(1,n+1))
arr.sort(reverse=True)
for i in range(n):print(*arr,sep=' ')