arr=[int(x) for x in input().split('\n')]
v=0
for i in arr:
    if i%3==0:
        v=1
        break
print(v)