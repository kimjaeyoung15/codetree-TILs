ages=list()
age=int()
while age<30:
    try:
        age=int(input())
        ages.append(age)
    except:break
ages=ages[:len(ages)-1]
print(f'{sum(ages)/len(ages):.2f}')