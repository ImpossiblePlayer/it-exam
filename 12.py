def f(s):
    while '15' in s or '255' in s or '555' in s:
        s = s.replace('15','2', 1)
        s = s.replace('255','1',1)
        s = s.replace('555','12',1)
    res =  sum(map(int,list(s)))
    return res

def prost(n):
    i = 2
    while i*i<=n:
        if n % i == 0:
            return False
        i += 1
    return True

mins=10000
for i2 in range(6,5000):
    for i1 in range(1):
        # if i1+i2>39:
        s='1'+'5'*i2+'2'+'5'*i2
        if(100<= f(s) <= 999):
            print(i2)
            # summa = i1+i2*2
            # if prost(f(s)):
            #     mins=min(summa,mins)
            
        # else:
            # break
# print(mins)
