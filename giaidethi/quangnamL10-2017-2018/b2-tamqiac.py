import math
#hàm tách số từ chuỗi
def TachSoTuChuoi(a):
    pat="0123456789"
    ret="0"
    for x in a:
        if x in pat:
            ret+=x
    return int(ret)
#test
print(TachSoTuChuoi("ádfdfdfs65f1654s1f65df4651"))
#hàm kiểm tra tam giác
def KiemTraTamGiac(a,b,c):
    if a==b==c: return "Tam giac deu"
    if a*a+b*b==c*c or b*b+c*c==a*a or a*a+c*c==b*b: return "Tam giac vuong"
    if a==b or b==c or c==a: return "Tam giac can"
    return "Tam giac thuong"
f=open("b2-tamgiac.inp")
[a,b,c]=map(lambda x:TachSoTuChuoi(x),f.read().split(";"))
f.close()
print(a,b,c)
p=(a+b+c)/2
s=round(math.sqrt(p*(p-a)*(p-b)*(p-c)),2)
ha=2*s/a
hb=2*s/b
hc=2*s/c
#ghi file
f=open("b2-tamgiac.out","w",encoding="UTF8")
f.writelines(KiemTraTamGiac(a,b,c)+"\n")
f.writelines(str(s)+"\n")
f.writelines(str(ha+hb+hc))
f.close()
