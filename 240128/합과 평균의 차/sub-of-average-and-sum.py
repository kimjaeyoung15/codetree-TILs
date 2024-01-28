arr=[int(i) for i in input().split()]
sumarr=sum(arr)
meanarr=int(sum(arr)/len(arr))
print(f'{sumarr}\n{meanarr}\n{sumarr-meanarr}')