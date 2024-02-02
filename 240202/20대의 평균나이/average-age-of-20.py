ages=list()
age=int()
while age<30:
    age=int(input())
    ages.append(age)
ages=ages[:len(ages)-1]
print(f'{sum(ages)/len(ages):.2f}')