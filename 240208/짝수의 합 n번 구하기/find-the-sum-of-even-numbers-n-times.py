n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    arr=[x for x in range(a,b+1)]
    if arr[0]%2==0:arrn=arr[0::2]
    else:arrn=arr[1::2]
    print(sum(arrn))