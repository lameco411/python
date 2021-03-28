f=open('daytang.inp')
n=f.readline().strip()
mangbandau=list(map(lambda x:int(x),f.readline().split()))
f.close()
print(mangbandau)
mangdaysotang=[]
for i in range(len(mangbandau)-1):
    mangtam=[]
    mangtam.append(mangbandau[i])
    for j in range(i,len(mangbandau)-1):
        if mangbandau[j+1]>mangbandau[j]:
            mangtam.append(mangbandau[j+1])
        else:
            break
    if len(mangtam)>=2:
        mangdaysotang.append(mangtam)
print(mangdaysotang)
#tìm mảng dài nhất trong dãy số tăng
mangketqua=[]
for x in mangdaysotang:
    if len(x)>=len(mangketqua):
        mangketqua=x
print(mangketqua)
# in vào file kết quả thôi nào
f=open('daytang.out','w')
f.writelines(str(len(mangketqua))+"\n")
f.writelines(" ".join(list(map(lambda x:str(x),mangketqua))))
f.close()