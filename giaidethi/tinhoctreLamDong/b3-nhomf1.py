f = open("b3-nhomf1.inp")
n=int(f.readline())
a=list(map(lambda x:x.split(),f.readlines()))
f.close()
#print(n,a)
def KiemTraCapKhongQuenBiet(a,i,j):
    if a[i][j]=='0' and a[j][i]=='0':
        return True
    return False
nhom1=[]
nhom2=[]
for i in range(n):
    if len(nhom1)==0:
        nhom1.append(str(i+1))
    else:
        for x in range(len(nhom1)):
            if KiemTraCapKhongQuenBiet(a,i,x)==False:
                nhom2.append(str(i+1))
                break
        else:
            nhom1.append(str(i+1))
print(nhom1)
print(nhom2)
f=open('b3-nhomf1.out','w')
f.writelines(" ".join(nhom1))
f.writelines('\n')
f.writelines(" ".join(nhom2))
f.close()