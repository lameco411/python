f=open('phanbiet.inp')
n=f.readline()
mangbandau=f.readline().split()
f.close()
# hàm kiểm tra sự tồn tại của phần tử trong list
def CheckExist(item,array):
    for x in array:
        if x==item:
            return True
    return False
mangketqua=[]
for x in mangbandau:
    if not CheckExist(x,mangketqua):
        mangketqua.append(x)
#print(mangketqua)
f=open('phabiet.out','w')
f.writelines(str(len(mangketqua))+"\n")
f.writelines(" ".join(mangketqua))
f.close()