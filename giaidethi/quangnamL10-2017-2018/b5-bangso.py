#hàm tìm số lớn nhất trong mảng
def FindMax(a):
    m =a[0]
    for i in  a:
        if i>m:m=i
    return m
f = open("b5-bangso.inp")
n=int(f.readline())
a=list(map(lambda x:int(x),f.readline().split()))
f.close()
print(n)
print(a)
#tìm tất cả các mảng có thể có
ketqua=[]
for i in range(FindMax(a),sum(a)): #số tổng có thể từ số lớn nhất tới tổng của mảng
    print("Giá trị số tổng: ",i)
    kq1=[]     
    x=0
    y=1
    while x<=y and y<=n:
        print(f"x:{x}, y:{y},tong x:y:{sum(a[x:y])}")
        if sum(a[x:y])==i:
            kq1.append(a[x:y])
            print(a[x:y])
            x=y
            y=x+1
        else:
            y+=1
    if len(kq1)>0:
        ketqua.append(kq1)
print(ketqua)
#tìm ra mảng nào có chiều dài nhất và bằng mảng gốc ( là đủ số)
mangketquacuoicung=ketqua[0]
for x in ketqua:    
    if sum(map(lambda x:sum(x),x))==sum(a) and len(x)>len(mangketquacuoicung):
        mangketquacuoicung=x
print(mangketquacuoicung)

#ghi vào file
f=open("b5-bangso.out","w",encoding="UTF8")
f.writelines(str(len(mangketquacuoicung)))
f.close()