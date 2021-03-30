f=open('average.inp')
n,k=map(lambda x:int(x),f.readline().split())
a=list(map(lambda x:int(x),f.readline().split()))
def average(a):
    n=0
    for i in range(len(a)):
        n+=a[i]
    return n/len(a)
ketqua=[]
for i in range(n):
    mang=[]
    for j in range(i,n):
        mang.append(a[j])
        if average(mang)==k:
            if len(ketqua)<len(mang):
                ketqua=mang.copy() 
            print(mang)
print(ketqua)
f.close()
f=open('average.out','w')
f.write(str(len(ketqua)))
f.close()