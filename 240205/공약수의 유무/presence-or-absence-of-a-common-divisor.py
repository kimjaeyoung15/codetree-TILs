a,b=map(int, input().split())
i=a
v=0
while i<b:
    if 1920%i==2880%i and 1920%i==0:
        v=1
        break
    i+=1
print(v)