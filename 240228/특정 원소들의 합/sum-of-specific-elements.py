arr=[[0]*4 for _ in range(4)]
sum=0
for i in range(4):
    arr[i]=[int(x) for x in input().split()]
for p in range(4):
    for j in range(p,4):
        sum+=arr[j][p]
print(sum)