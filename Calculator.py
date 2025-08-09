def bagi(a, b):
    if b == 0:
        return "Error the number divided cannot be zero"
    return a / b

def kali(a, b):
    return a * b

def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def bagi_float(a , b):
    if b == 0:
        return "Error the number divided cannot be zero"
    return  a // b

def sisa(a, b):
    return a % b

def pangkat(a, b):
    return a ** b

while True:
    n1 = int(input("Enter your number here: "))
    mark =  input("Enter your mark here: ")
    n2 = int(input("Enter your designated number to be multiplied or anything is that: "))

    if mark == "+":
        print(tambah(n1, n2))
    elif mark == "-":
        print(kurang(n1, n2))
    elif mark == "*":
        print(kali(n1, n2))
    elif mark == "/":
        print(bagi(n1, n2))
    elif mark == "//":
        print(bagi_float(n1, n2))
    elif mark == "**":
        print(pangkat(n1, n2))
    elif mark == "%":
        print(sisa(n1, n2))
    else:
        print("An error has occurred")
        break

