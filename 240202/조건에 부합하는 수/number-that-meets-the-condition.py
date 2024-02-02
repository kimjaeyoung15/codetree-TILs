a=int(input())
nr=list()
for i in range(1,a+1):
    if (i%2!=0 or i%4==0) and (i//8)%2!=0 and i%7>=4:nr.append(i)
print(*nr, sep=' ')