# bài toán liên quan tới đếm cách là bài toán sử dụng quy hoạch động
f=open('change.inp')
n,k = map(lambda x:int(x),f.readline().split())
ks=[x+1 for x in range(k)]
def change(n,k): 
    def ways(amount,arrays,i):
        if amount==0:return 1
        if amount<0 or len(arrays)==0:return 0
        if (amount,i) not in res:
            res[(amount,i)]=ways(amount-arrays[-1],arrays,i)+ways(amount,arrays[:-1],i-1)
        return res[(amount,i)]
    res={}
    return ways(n,k,len(k)-1)
print(change(n,ks))