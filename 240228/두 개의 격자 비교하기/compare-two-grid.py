a,b=map(int,input().split())
arr1=[[0]*b for _ in range(a)]
arr2=[[0]*b for _ in range(a)]
comp=[[0]*b for _ in range(a)]
for i in range(a):
    arr1[i]=[int(x) for x in input().split()]
for j in range(a):
    arr2[j]=[int(x) for x in input().split()]
for x in range(a):
    for y in range(b):
        if arr1[x][y]==arr2[x][y]:comp[x][y]=0
        else:comp[x][y]=1
for k in range(a):
    print(*comp[k],sep=' ')