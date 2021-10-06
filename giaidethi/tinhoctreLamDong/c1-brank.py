#đọc file
f=open('c1-brank.inp')
#destructuring 
n,m=map(lambda x:int(x),f.readline().split())
# đọc tất cả các dòng còn lại
a=list(map(lambda x:x.split(),f.readlines()))
#đóng file
f.close()
'''
Biết được thứ hạng của mình thì phải so sánh với n-1 người
hoặc là:
1. Mình so sánh với người đã biết thứ hạng rồi, mà người đó là số 2 và mình hơn người đó
2. mình so sánh với người đã biết thứ hạng rồi, mà người đó là thứ n-1 và mình nhỏ hơn người đó
'''
array=[]
for i in range(n):  
    array.append({'rank': 0, 'number': 0, 'greater': 0, 'less': 0, 'last': False, 'first': False})
def SoSanh(a,b):
    a=a-1
    b=b-1
    array[a]["less"]+=1
    array[b]["greater"]+=1
    array[a]["number"]+=1
    array[b]["number"]+=1
    if array[a]["less"]+array[a]["greater"]==n-1:
        array[a]["rank"]=array[a]["greater"]+1
    if array[b]["less"]+array[b]["greater"]==n-1:
        array[b]["rank"]=array[b]["greater"]+1
    if array[a]["rank"]==n-1:
        array[b]["last"]=True
    if array[b]["rank"]==2:
        array[a]["rank"]=True
SoSanh(4,3)
SoSanh(4,2)
SoSanh(3,2)
SoSanh(1,2)
SoSanh(2,5)
sohocsinhbietduocthuhang=0
for x in array:
    if x["rank"]!=0 or x["last"]==True or x["first"]==True:
        sohocsinhbietduocthuhang+=1
print(sohocsinhbietduocthuhang)
f=open("c1-brank.out",'w')
f.writelines(str(sohocsinhbietduocthuhang))
f.close()
'''
Khởi tạo một mảng học sinh
viết hàm để kiểm tra 2 số
đưa những so sánh vào để kiểm tra
sau mỗi lần đưa vào kiểm tra thì sẽ có những thay đổi trong mỗi học sinh như sau
- hạng của chính mình
- số lượng so sánh
- là hạng chót khi người mình so sánh là áp chót và lớn hơn mình
- là lạng nhất khi biết người mình so sánh là hạng 2 và nhỏ hơn mình
'''