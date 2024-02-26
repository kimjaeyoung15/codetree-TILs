a,b=map(int, input().split())
divd,dvsr=a,b
sumsq=0
res=[0 for _ in range(11)]
while True:
    res[divd%dvsr]+=1
    divd=divd//dvsr
    if divd<=1:
        break
for i in res:
    sumsq+=i**2
print(sumsq)