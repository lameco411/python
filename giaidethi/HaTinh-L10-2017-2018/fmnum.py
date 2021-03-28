f=open('fmnum.inp')
n,s=map(lambda x:int(x),f.readline().split())
print(n,s)
mang=[0 for x in range(n)]
mangketqua=[]
def attemp(i):    
    for x in range(1 if i==0 else 0,10):
        mang[i]=x
        if i>=n-1:
            k=0
            for j in range(n):
                k+=mang[j]
            if k==s:
                #nếu map qua mảng mới thì ok, còn append trực tiếp thì nó append kết quả cuối cùng
                mangketqua.append(" ".join(map(lambda x:str(x),mang)))            
                print(mang)                          
        else:
            attemp(i+1)
attemp(0)
print(mangketqua[0])
f.close()
f=open('fmnum.out','w')
f.write(mangketqua[0])
f.close()