n=int(input())
arr=[int(x) for x in input().split()]
arr.sort()
diff=list()
for i in range(n-1):
    diff.append(arr[i+1]-arr[i])
print(min(diff))