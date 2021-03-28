f=open('expr.inp')
n,k=map(lambda x:int(x),f.readline().split())
mang=f.readline().split()
#print(n,k,mang)
toantu=['+','-']
a=['0' for x in range(n-1)]
#print(a)
ketqua=[]
def attemp(i):
    for v in range(2):
        a[i]=toantu[v]
        if i>n-3:
            tong=mang[0]
            for x in range(n-1):
                tong+=a[x]+mang[x+1]
            if eval(tong)==k:
                ketqua.append("".join(a))
        else:
            attemp(i+1)
attemp(0)
print(ketqua)
f.close()
f=open('expr.out','w')
f.write(ketqua[0])
f.close()