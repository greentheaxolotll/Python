def main():
    user_time = input("Enter a time (HH:MM): ")
    time_decimal = convert(user_time)
    if 7.0 <= time_decimal <= 8.0:
        print("breakfast time")
    elif 12.0 <= time_decimal <= 13.0:
        print("lunch time")
    elif 18.0 <= time_decimal <= 19.0:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + float(minutes) / 60

if __name__ == "__main__":
    main()
