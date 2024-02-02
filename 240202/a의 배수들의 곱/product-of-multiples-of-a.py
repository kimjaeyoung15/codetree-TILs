a,b=map(int,input().split())
nr=list()
prod=1
for i in range(1,b+1):
    if i%a==0:nr.append(i)
for j in nr:prod*=j
print(prod)