n=int(input())
a=list()
for i in range(n):
    tmp=int(input())
    a.append(tmp)
for j in a:
    if j%2==1 and j%3==0:print(j)