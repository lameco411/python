f=open("b2-covid.inp")
a=list(map(lambda x:x.strip().split(), f.readlines()))
f.close()
print(a)
def thoigiancho(n,t):
    if t>=5: return 0
    else:
        return (n-1)*(5-t)
print(thoigiancho(50000,2))

f=open("b2-covid.out","w")
for x in a:
    f.writelines(str(thoigiancho(int(x[0]),int(x[1]))))
    f.writelines("\n")
f.close()