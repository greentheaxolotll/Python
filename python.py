yell = input ("Input: ")
print(yell.lower())

slow = input ("Input: ")
slowreal = slow.replace(" ", "...")
print(slowreal)

def calculate_weight(a):
    weight = a * 0.378
    return weight
e_weight = int(input("Earth weight: "))
m_weight = calculate_weight(e_weight)
print("Weight on Mars: " + str(m_weight))

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    return float(d.lstrip("$"))


def percent_to_float(p):
    return float(p.strip("%")) / 100

main()
