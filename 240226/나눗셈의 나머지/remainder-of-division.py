a,b=map(int, input().split())
divd,dvsr=a,b
sumsq=0
res=[0 for _ in range(9)]
while True:
    divd=divd//dvsr
    res[divd%dvsr-1]+=1
    if divd==0:
        break
for i in res:
    sumsq+=i**2
print(sumsq)