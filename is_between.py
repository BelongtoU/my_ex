ip = input("Nhap vao 3 so x, y, z: ")
ip_list = ip.split()


def isbetween(x, y, z):
    return (y <= x) and (x <= z)

print("         So x co nam giua y va z ???????  %s"%isbetween(ip_list[0], ip_list[1], ip_list[2]))