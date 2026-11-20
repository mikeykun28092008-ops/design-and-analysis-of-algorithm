def karatsuba(x, y):
    if x < 10 or y < 10: return x*y
    n=max(len(str(abs(x))), len(str(abs(y))))
    half=n//2
    power=10**half
    a,b=divmod(x,power); c,d=divmod(y,power)
    z0=karatsuba(b,d)
    z2=karatsuba(a,c)
    z1=karatsuba(a+b,c+d)-z2-z0
    return z2*power*power + z1*power + z0

if __name__ == "__main__":
    print(karatsuba(1234, 5678))
