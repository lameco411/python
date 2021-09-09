f = open("b1-doben.inp")
n=f.readline().strip()
f.close()

def doben(n):   
    if len(n)==1:
        return 0    
    else:
        while len(n)>=2:
            r=1
            for x in n:
                r*=int(x)
            n=str(r+1)
        return str(n) 

f=open("b1-doben.out","w")
f.writelines(doben(n))
f.close()