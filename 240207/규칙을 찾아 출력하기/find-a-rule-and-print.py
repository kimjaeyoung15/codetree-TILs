n=int(input())
for p in range(n):print('* ',end='')
print()
for i in range(n-1):
    for x in range(i+1):print('* ',end='')
    for y in range((n-2-i)*2):print(' ',end='')
    print('*')