import math 

str_1 = input("Nhap toa do A(a1, a2): ")
str_2 = input("Nhap toa do B(b1, b2): ")
A = str_1.split()
B = str_2.split()

for i in range(2):
    A[i] = float(A[i])
    B[i] = float(B[i])

def slope (x1, x2, y1, y2):
    cos = abs(x1 - x2)/math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return cos


def intercept (x0, y0):
    b = y0 - slope(A[0], B[0], A[1], B[1])*x0
    return b 


z = intercept(A[0], A[1])

if z >= 0:
    print("Duong thang qua A(%s, %s) va B(%s, %s) la: \n"%(A[0], A[1], B[0], B[1]))
    print("                 y = %sx + %s"%(slope(A[0], B[0], A[1], B[1],), z))
else:
    print("Duong thang qua A(%s, %s) va B(%s, %s) la: \n"%(A[0], A[1], B[0], B[1]))
    print("                 y = %sx - %s"%(slope(A[0], B[0], A[1], B[1],), abs(z)))