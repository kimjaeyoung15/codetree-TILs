nr=list()
even=0
for i in range(5):
    tmp=int(input())
    nr.append(tmp)
for j in nr:
    if j%2==0:even+=1
print(even)