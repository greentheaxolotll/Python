num = str(input("Input: "))
x, y, z = num.split(" ")
if y == "+":
    print(int(x) + int(z))
elif y == "-":
    print(int(x) - int(z))
elif y == "*":
    print(int(x) * int(z))
elif y == "/":
    print(int(x) / int(z))
elif z == "0":
    print("Invalid input")