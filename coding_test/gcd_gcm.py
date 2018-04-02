# 최소공배수, 최대공약수

def gcd(m,n):

    while True:
        r = m % n
        if r == 0:
            return n
        else:
            m = n
            n = r



def gcm(m,n):
    return int(m*n/gcd(m,n))



print(gcd(5,15))
print(gcm(3,7))