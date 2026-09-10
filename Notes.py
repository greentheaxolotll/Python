
#If statements in Python

x = int(input("what's x? "))
y = int(input("what's y? "))

if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
elif x == y:
    print("x is equal to y")
else:
    print("Invalid input")

#Age checker

age = int(input("how old are you? "))

if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 55:
    print("You are an adult.")
elif age >= 55:
    print("You are a senior citizen.")

#Even or odd number checker

num = int(input("what number do you want to check? "))

if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")

#boolean expressions

a = 15
b = 8

c = a == b

if c == True:
    print("a is equal to b")
else:
    print("a is not equal to b")

#match statements

amount = 10

match amount:
    case 5:
        print("nickel")
    case 10:
        print("dime")
    case 25:
        print("quarter")