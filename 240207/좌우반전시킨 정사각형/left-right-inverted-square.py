n=int(input())
arr=list(range(1,n+1))
arr.sort(reverse=True)
for i in range(1,n+1):
    for j in arr:
        print(j*i,end=' ')
    print()