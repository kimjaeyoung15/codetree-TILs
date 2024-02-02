nr=[int(x) for x in input().split()]
print(1,end=' ') if nr[1]==min(nr) else print(0,end=' ')
print(1) if nr[1]==nr[2] and nr[1]==nr[3] else print(0)