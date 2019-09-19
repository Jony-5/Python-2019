# bincon.py JM
# convert a bas 10 number to binary
# use 191 base 10 equal to 1011 1111 base
# q(quotient) d(divisor) r(remainder) n(integer input)
# div 128
n = int(input("Input and integer less than 256 ; "))
d = 128	
q = int(n / 128)
r = int(n % 128)
print(d,q,r)
n = r
# div 64
d = int(d / 2)
q = int(n / d)
r = int(n % d)
print(d,q,r)
n = r
# div 32
d = int(d / 2)
q = int(n / d)
r = int(n % d)
print(d,q,r)
n = r
#div 16
d = int(d / 2)
q = int(n / d)
r = int(n % d)
print(d,q,r)
n = r
#div 8
d = int(d / 2)
q = int(n / d)
r = int(n % d)
print(d,q,r)
n = r
#div 4
d = int(d / 2)
q = int(n / d)
r = int(n % d)
print(d,q,r)
n = r
#div 2
d = int(d / 2)
q = int(n / d)
r = int(n % d)
print(d,q,r)
n = r
#div 1d = int(d / 2)
q = int(n / d)
r = int(n % d)
print(d,q,r)
n = r
