f=open('matran.inp')
m,n=map(lambda x:int(x),f.readline().split())
mang=f.read().split()
print(m,n,mang)
def solelonnhat(a):
    kq=0
    for x in a:
        if int(x)%2==1 and int(x)>kq:
            kq=int(x)
    return str(kq)
def sochannhonhat(a):
    kq=1000000
    for x in a:
        if int(x)%2==0 and int(x)<kq:
            kq=int(x)
    return str(kq)
print(solelonnhat(mang))
print(sochannhonhat(mang))
mangketqua=[['0' for x in range(n)] for y in range(m)]
k=1
for i in range(m):
    for j in range(n):  
        if k%2==1:     
            mangketqua[i][j]=solelonnhat(mang)
            mang.remove(solelonnhat(mang))      
        else:
            mangketqua[i][j]=sochannhonhat(mang)
            mang.remove(sochannhonhat(mang))  
        k+=1   
        
ketqua=list(map(lambda x:" ".join(x),mangketqua))
f.close()
f=open('matran.out','w')
f.write('\n'.join(ketqua))
f.close()
