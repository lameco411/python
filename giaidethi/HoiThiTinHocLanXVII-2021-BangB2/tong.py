f=open('tong.inp')
n=f.readline().strip()
tong=0
solonnhat=0
for x in n:
    tong+=int(x)
    if int(x)>solonnhat:
        solonnhat=int(x)
print(tong)
print(solonnhat)
f.close()
f=open('tong.out','w')
f.writelines(str(tong)+"\n")
f.writelines(str(solonnhat))
f.close()
