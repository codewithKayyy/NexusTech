def age_calculation():
    age = int(input("How old are you? "))
    if age > 15:
        print("You are {} years!".format(age+1))
    elif age <= 15:
        print("You are {} years!".format(age))


if __name__ == "__main__":
    age_calculation()