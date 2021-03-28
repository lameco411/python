f=open('biop.inp')
n=int(f.readline().strip())
prices=list(map(lambda x:int(x),f.readline().split()))
print(n,prices)
ketqua=[]
for i in range(n):
    inc=0
    dec=0
    for j in range(n):
        if prices[j]>prices[i]:
            inc+=1
        elif prices[j]<prices[i]:
            dec+=1
    ketqua.append(str(dec)+" "+str(inc))
print(ketqua)
f.close()
f=open('biop.out','w')
f.write('\n'.join(ketqua))
f.close()