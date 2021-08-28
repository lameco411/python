#hàm chuyển mã ký tự
def ChuyenMa(s,n):
    a=ord(s)    
    r= a-n if a -n>=65 else a-n+24
    return chr(r)
#hàm chuyển mã một chuỗi
def ChuyenMaChuoi(s,n):
    r=""
    for x in s:
        r+=ChuyenMa(x,n)
    return r
f= open("b4-giaima.inp")
n=int(f.readline())
arr=list(f.readline().split())
print(n)
print(arr)
f.close()
ketqua=[]
for i in range(len(arr)):
    ketqua.append(ChuyenMaChuoi(arr[i],n))
f=open("b4-giaima.out","w",encoding="UTF8")
f.write(" ".join(ketqua))
f.close()