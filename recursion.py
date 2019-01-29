ip = int(input("Countdown from: "))

print()
print()
print()

def countdown (x):
    if x == 0:
        print()
        print()
        print()
        print("-----***-----    Blastoff !!!    -----***-----")
        print()
        print()
        print()
        return
    else:
        print("         ", x)
        countdown(x-1)

countdown(ip)