import itertools
f = open('caphe.inp')
dong1=f.readline().split(' ')
n=int(dong1[0])
m=int(dong1[1])
danhsachbao=list(map(lambda a:int(a), f.readline().split(' ')))
a=[0]*n
ketqua=[]
lim=[int(m/x) for x in danhsachbao]
def attempt(i):
    for v in range(lim[i]+1):
        a[i]=v
        if i>=n-1:
            k=0
            for x in range(n):
                k+=a[x]*danhsachbao[x]
            if k==m:                        
                print(a)
                ketqua.append(" ".join(list(map(lambda y:str(y),a))))
                k=0
                
        else:
            attempt(i+1)
attempt(0)
print(ketqua)
f=open('caphe.out',mode="w")
if len(ketqua)==0:
    f.write('NO')
else:
    f.write('\n'.join(ketqua))
f.close()
