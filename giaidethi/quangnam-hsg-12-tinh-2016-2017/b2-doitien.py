f=open("b2-doitien.inp")
[n,m]=map(lambda x:int(x),f.readline().split())
a=list(map(lambda x:int(x),f.readline().split()))
f.close()
print(n,m)
a.reverse()
print(a)
soluongtien=[0 for x in a]
print(soluongtien)
for i in range(n):
    soluongtien[i]=int(m/a[i])
    m=m%a[i]    
print(soluongtien)
soluongtien.reverse()
#ghi file
f=open("b2-doitien.out","w",encoding="UTF8")
f.writelines("-1" if m!=0 else str(sum(soluongtien))+"\n")
f.writelines("" if m!=0 else " ".join(list(map(lambda x:str(x),soluongtien))))
f.close()