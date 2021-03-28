#hàm tìm giá trị lớn nhất trong mảng 2 chiều
def FindMax(array):
    ketqua=100
    for i in array:
        for j in i:
            if int(j)<ketqua:
                ketqua=int(j)
    return ketqua
f=open('matran.inp')
n,m,k=list(map(lambda x:int(x),f.readline().split()))
#print(n,m,k)
matranbandau=list(map(lambda x:x.split(),f.readlines()))
f.close()
#print(matranbandau)
ketqua=0
a=[[0]*k for i in range(k)]
for i in range(n-k+1):
    for j in range(m-k+1):                
        for y in range(k):
            for z in range(k):
                #print(y,z)
                #print(matranbandau[i+y][j+z])
                a[y][z]=matranbandau[i+y][j+z]
        if FindMax(a)>ketqua:
            ketqua=FindMax(a)
print(ketqua)
f=open('matran.out','w')
f.write(str(ketqua))
f.close()