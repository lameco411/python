f=open('mang.inp')
n=int(f.readline())
mang=list(map(lambda x:int(x),f.readline().split()))
#print(n,mang)
sonhonhat=mang[0]
vitri=0
for i in range(1,len(mang)):
    if mang[i] <sonhonhat:
        sonhonhat=mang[i]
        vitri=i
print(vitri+1)
f.close()
f=open('mang.out','w')
f.writelines(' '.join(map(lambda x:str(x),mang))+"\n")
f.writelines(str(vitri+1))
f.close()