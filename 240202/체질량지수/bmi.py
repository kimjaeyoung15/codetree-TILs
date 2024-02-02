ht,wt=map(int, input().split())
bmi=int(wt/(ht/100)**2)
print(bmi)
if bmi>=25:print("Obesity")