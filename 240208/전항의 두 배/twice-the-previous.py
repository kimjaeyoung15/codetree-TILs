prog=[int(x) for x in input().split()]
for i in range(8):
    prog.append(2*prog[i]+prog[i+1])
print(*prog,sep=' ')