arr=[]
for x in range(5):
    tmp=int(input())
    arr.append(tmp)
v=0
for i in arr:
    if i%3==0:
        v=1
        break
print(v)