n=int(input())
asc=int(65)
for i in range(n,0,-1):
    for p in range((n-i)*2):print('',end=' ')
    for x in range(i):
        
        if asc!=90:
            print(chr(asc),end=' ')
            asc+=1
        else:
            print(chr(asc),end=' ')
            asc=65
    print()