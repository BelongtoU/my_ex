x_ip = int(input("Nhap co bang: "))
x_list = []
result = []
for i in range(x_ip):
    x_list.append(i+1)
def nhan(ip, ipo):
    r_list = []
    for i in range(1, ip + 1):
        a = ipo*x_list[i-1]
        r_list.append(a)
    return r_list
def multiple_list(x):
    for z in range(1, x+1):
        s = nhan(x, z)
        print(z, end = "\t")               
        for i in range(x):
            print(s[i], end = "\t")
        print("\n")
print("       ", end = " ")
for i in range(1, x_ip+1):
    print(i, end = "\t")
print("\n")
multiple_list(x_ip)