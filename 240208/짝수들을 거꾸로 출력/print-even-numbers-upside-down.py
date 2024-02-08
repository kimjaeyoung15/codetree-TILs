n=int(input())
arr=[int(x) for x in input().split()]
for i in range(len(arr)-1,-1,-1):
    if arr[i]%2==0:print(arr[i],end=' ')