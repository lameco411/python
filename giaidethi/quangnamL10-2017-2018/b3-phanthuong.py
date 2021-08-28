#hàm ước chung lớn nhất của 2 số
def UCLN(a,b):
    while a!=b:
        if a>b: a=a-b
        if b>a: b=b-a
    return a
f = open("b3-phanthuong.inp")
n=int(f.readline())
arr=list(map(lambda x:int(x),f.readline().split()))
f.close()
#tìm phần tử lớn nhất trong mảng
m=UCLN(arr[0],arr[1])
for i in range(2,len(arr)):
    m=UCLN(m,arr[i])
print(m)
# tạo file nếu chưa có, nếu có thì mở lên
f=open("b3-phanthuong.out","w",encoding="UTF8")
f.write(str(m))
f.close()