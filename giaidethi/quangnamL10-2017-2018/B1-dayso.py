#hàm kiểm tra số nguyên tố
def KiemTraSoNguyenTo(n):
    if n<=3: 
        return True
    #tìm những điều kiện cơ bản dự đoán được để giảm bớt vòng lặp for
    elif n%2==0 or n%3==0: 
        return False
    i=5
    while i*i<=n:
        #Kiểm tra các số có dạng 6k ± 1 từ 2 đến √n
        if n%i ==0 or n%(i+2)==0:return True
        i+=6
    return True
#hàm kiểm tra số lượng số nguyên tốt trong một mảng
def DemSoNguyenTo(a):
    n=0
    for x in a:
        if KiemTraSoNguyenTo(x):
            n+=1
    return n
#hàm kiểm tra tính đơn điệu tăng
def KiemTraTangDan(a):
    for i in range(len(a)):
        if a[i+1]<a[i]: #chỉ cần không thỏa điều kiện thì trả về false
            return False
    #vượt qua hết các vòng là đủ điều kiện, trả về true
    return True
f = open("b1-dayso.inp")
#lấy dòng đầu tiên
n=int(f.readline())
#lấy đong kế và chuyển thành mảng số nguyên
a=list(map(lambda x:int(x),f.readline().split()))
f.close()
print(n)
print(a)
# trung bình trong dãy a
average=sum(a)/n
print(average)


#mở file để ghi
f=open("B1-dayso.out","w",encoding="UTF8")
f.writelines(str(round(average,2))+"\n")
f.writelines(str(DemSoNguyenTo(a))+"\n")
f.writelines(f"""Dãy số A {"là" if KiemTraTangDan(a) else "không là"} dãy đơn điệu tăng """)
f.close()