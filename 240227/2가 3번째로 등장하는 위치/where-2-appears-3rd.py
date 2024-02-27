n=int(input())
numbers=[int(x) for x in input().split()]
cnt=0
for i in range(len(numbers)):
    if numbers[i]==2:cnt+=1
    if cnt==3:break
print(i+1)