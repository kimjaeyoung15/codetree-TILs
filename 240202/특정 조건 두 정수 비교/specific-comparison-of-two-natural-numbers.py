a,b=map(int, input().split())
res=list()
if a<b:res.append(1)
else:res.append(0)
if a==b:res.append(1)
else:res.append(0)
print(*res, sep=' ')