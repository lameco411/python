import math
def KiemTraSoNguyenTo(n):
    if n<=3: 
        return "Yes"
    elif n%2==0 or n%3==0: #tìm những điều kiện cơ bản dự đoán được để giảm bớt vòng lặp for
        return "NO"
    i=5
    while i*i<=n:
        #Kiểm tra các số có dạng 6k ± 1 từ 2 đến √n
        if n%i ==0 or n%(i+2)==0:return "NO"
        i+=6
    return "Yes"
#print(KiemTraSoNguyenTo(17))
f=open('nguyento.inp')
n=f.readline().strip()
f.close()
tongchuso=0
for x in n:
    tongchuso+=int(x)
f=open('nguyento.out','w')
f.writelines(str(tongchuso)+"\n")
f.writelines(KiemTraSoNguyenTo(tongchuso))
f.close()