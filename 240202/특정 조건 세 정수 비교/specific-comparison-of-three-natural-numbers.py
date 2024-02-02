nr=[int(x) for x in input().split()]
print(1,end=' ') if nr[0]==min(nr) else print(0,end=' ')
print(1) if nr[0]==nr[1] and nr[0]==nr[2] else print(0)