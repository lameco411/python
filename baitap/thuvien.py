import math
#bài 1:
def bai1(n):
    if n>0: 
        kq=0
        for i in range(1,n+1):
            kq+=i
        return kq
    return "Số nhập vào không hợp lệ"
#bài 2
def bai2(n):
    if n>0: 
        kq=0
        for i in range(1,n+1):
            kq+=i*i
        return kq
    return "Số nhập vào không hợp lệ"
#bài 3
def bai3(n):
    if n>0: 
        kq=0
        for i in range(1,n+1):
            kq+=1/i
        return kq
    return "Số nhập vào không hợp lệ"
#bài 4
def bai4(n):
    if n>0: 
        kq=0
        for i in range(1,n+1):
            kq+=1/(2*i)
        return kq
    return "Số nhập vào không hợp lệ"
#bài 5
def bai5(n):
    if n>0: 
        kq=0
        for i in range(0,n+1):
            kq+=1/(2*i+1)
        return kq
    return "Số nhập vào không hợp lệ"
#bài 6
def bai6(n):
    if n>0: 
        kq=0
        for i in range(1,n+1):
            kq+=1/(i*(i+1))
        return kq
    return "Số nhập vào không hợp lệ"
#bài 7
def bai7(n):
    if n>0: 
        kq=0
        for i in range(1,n+1):
            kq+=i/(i+1)
        return kq
    return "Số nhập vào không hợp lệ"
#bài 8
def bai8(n):
    if n>0: 
        kq=0
        for i in range(0,n+1):
            kq+=(2*i+1)/(2*i+2)
        return kq
    return "Số nhập vào không hợp lệ"
#bài 9
def bai9(n):
    if n>0: 
        kq=1
        for i in range(1,n+1):
            kq*=i
        return kq
    return "Số nhập vào không hợp lệ"
#bài 10
def bai10(x,n):
    if n>0: 
        kq=1
        for i in range(1,n+1):
            kq*=i
        return kq
    return "Số nhập vào không hợp lệ"
#bài 11
def bai11(n):
    if n>0: 
        kq=0
        for i in range(1,n+1):
            kq+=bai9(i)
        return kq
    return "Số nhập vào không hợp lệ"
#bài 12
def bai12(x,n):
    if n>0: 
        kq=0
        for i in range(1,n+1):
            kq+=bai10(x,i)
        return kq
    return "Số nhập vào không hợp lệ"
#bài 13
def bai13(x,n):
    if n>0: 
        kq=0
        for i in range(1,n+1):
            kq+=bai10(x,2*i)
        return kq
    return "Số nhập vào không hợp lệ"
#bài 14
def bai14(x,n):
    if n>0: 
        kq=0
        for i in range(1,n+1):
            kq+=bai10(x,2*i+1)
        return kq
    return "Số nhập vào không hợp lệ"
#bài 15
def bai15(n):
    if n>0: 
        kq=0
        for i in range(1,n+1):
            kq+=1/bai1(i)
        return kq
    return "Số nhập vào không hợp lệ"
#bài 16
def bai16(x,n):
    if n>0: 
        kq=0
        for i in range(1,n+1):
            kq+=bai10(x,i)/bai1(i)
        return kq
    return "Số nhập vào không hợp lệ"
#bài 17
def bai17(x,n):
    if n>0: 
        kq=0
        for i in range(1,n+1):
            kq+=bai10(x,i)/bai9(i)
        return kq
    return "Số nhập vào không hợp lệ"
# bài 18
def bai18(x,n):
    if n>0: 
        kq=0
        for i in range(1,n+1):
            kq+=bai10(x,i*2)/bai9(i*2)
        return kq
    return "Số nhập vào không hợp lệ"
#bài 19
def bai19(x,n):
    if n>0: 
        kq=0
        for i in range(0,n+1):
            kq+=bai10(x,i*2+1)/bai9(i*2+1)
        return kq
    return "Số nhập vào không hợp lệ"
# Hàm kiểm tra ước số:
def KiemTraUocSo(x,n):
    if n%x==0:
        return True
    return False
# bài 20: Liệt kê tất cả ước số của số nguyên dương n
def bai20(n):
    if n>0: 
        kq=[]
        for i in range(1,n+1):
            if KiemTraUocSo(i,n):
                kq.append(i)
        return kq
    return "Số nhập vào không hợp lệ"
#bài 21: Tính tổng tất cả ước số của số nguyên dương n
def bai21(n):
    if n>0: 
        kq=0
        for x in bai20(n):
            kq+=x
        return kq
    return "Số nhập vào không hợp lệ"
#bài 21: Tính tích tất cả ước số của số nguyên dương n
def bai22(n):
    if n>0: 
        kq=1
        for x in bai20(n):
            kq*=x
        return kq
    return "Số nhập vào không hợp lệ"
#bài 23: Đếm số lượng ước số của số nguyên dương n
def bai23(n):
    return len(bai21(n))
#bài 24: Liệt kê tất cả ước số lẻ của số nguyên dương n
def bai24(n):
    if n>0: 
        kq=[]
        for i in range(1,n+1):
            if KiemTraUocSo(i,n) and i%2==1:
                kq.append(i)
        return kq
    return "Số nhập vào không hợp lệ"
#Bài 25 Tính tổng tất cả ước số chẵn của số nguyên dương n
def bai25(n):
    if n>0: 
        kq=0
        for i in range(1,n+1):
            if KiemTraUocSo(i,n) and i%2==0:
                kq+=i
        return kq
    return "Số nhập vào không hợp lệ"
#bài 26: Tính tích tất cả ước số lẻ của số nguyên dương n
def bai26(n):
    if n>0: 
        kq=1
        for i in range(1,n+1):
            if KiemTraUocSo(i,n) and i%2==1:
                kq*=i
        return kq
    return "Số nhập vào không hợp lệ"
#bài 27: đếm số lượng ước số chẵn của số nguyên dương n
def bai27(n):
    if n>0: 
        kq=0
        for i in range(1,n+1):
            if KiemTraUocSo(i,n) and i%2==0:
                kq+=1
        return kq
    return "Số nhập vào không hợp lệ"
#bài 28:Cho số nguyên dương n. tính tổng các ước số nhỏ hơn chính nó
def bai28(n):
    if n>0: 
        kq=0
        for i in range(1,n):
            if KiemTraUocSo(i,n):
                kq+=i
        return kq
    return "Số nhập vào không hợp lệ"
#bài 29: tìm ước số lẻ lớn nhất của số nguyên dương n
def bai29(n):
    if n>0: 
        kq=1
        for i in range(1,n):
            if KiemTraUocSo(i,n) and i%2==1:
                kq=i
        return kq
    return "Số nhập vào không hợp lệ"
#bài 30: Cho số nguyên dương n. Kiểm tra số n có phải là số hoàn thiện hay không?
# số hoàn thiện là gì?
# Số hoàn thiện là tổng các ước nhỏ hơn nó bằng chính nó
def bai30(n):
    if bai28(n)==n:
        return True
    return False
#bài 31: Cho số nguyên dương n. Kiểm tra số nguyên dương n có phải là số nguyên tố hay không
def KiemTraSoNguyenTo(n):
    if n>0:
        if n<=2: return True
        for i in range(2,int(math.sqrt(n))):
            if n%i==0:
                return False
        return True
    return "Số nhập vào không hợp lệ"
#bài 33
def bai33(n):
    if n>0:
        kq=math.sqrt(2)
        for i in range(1,n):
            kq=math.sqrt(kq)
        return kq  
    return "Số nhập vào không hợp lệ"
   
#bài 34
def bai34(n):
    if n>0:
        kq=1
        for i in range(2,n+1):
            kq=math.sqrt(kq+i)
        return kq
    return "Số nhập vào không hợp lệ"
#bài 35:
def bai35(n):
    if n>0:
        kq=n
        for i in range(n,0,-1):
            kq=math.sqrt(i+kq)
        return kq
    return "Số nhập vào không hợp lệ"
#Giai thừa
def GiaiThua(n):
    if n>=0:
        if n==1 or n==0:return 1
        else:
            return GiaiThua(n-1)*n
    return "Số nhập vào không hợp lệ"    
#Bài 36:
def bai36(n):
    kq=1
    for i in range(2,n+1):
        kq=math.sqrt(kq+GiaiThua(i))
    return kq
#bài 37:
def bai37(n):
    if n>2:
        kq=math.sqrt(2)
        for i in range(3,n):
            kq=math.pow(kq+i,1/i)
    return "Số nhập vào không hợp lệ"
#bài 38
def bai38(n):
    if n>0:
        kq=1
        for i in range(2,n+2):
            kq=math.pow(i+kq,1/(i+1))
        return kq
    return "Số nhập vào không hợp lệ"
#bài 39;
def bai39(n):
    if n>0:
        kq=1
        for i in range(2,n+2):
            kq=math.pow(GiaiThua(i)+kq,1/(i+1))
        return kq
    return "Số nhập vào không hợp lệ"
#bài 40
def bai40(x,n):
    kq=x
    for i in range(2,n+1):
        kq=math.sqrt(math.pow(x,i)+kq)
#bài 41
def bai41(n):
    kq=1
    for i in range(n):
        kq=1/(1+kq)
    return kq
