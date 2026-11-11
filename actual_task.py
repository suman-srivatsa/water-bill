def calculate_charge(units):
    if units <= 10:
        charge = units * 6
    elif units <= 25:
        charge = (10 * 6) + (units - 10) * 9
    else:
        charge = (10 * 6) + (15 * 9) + (units - 25) * 12

    if units <= 10:
        charge = charge - (charge * 0.10)

    return charge


def usage_category(units):
    if units <= 10:
        return "Eco Friendly"
    elif units <= 25:
        return "Normal Usage"
    else:
        return "Heavy Usage"


def conservation_tip(category):
    if category == "Eco Friendly":
        return "Congratulations! You receive a 10% discount."
    elif category == "Normal Usage":
        return "Use water carefully to save money."
    else:
        return "Reduce water consumption to avoid high bills."


print("     SMART WATER BILL SYSTEM")

name = input("Enter Consumer Name: ")
units = float(input("Enter Water Usage: "))

if units < 0:
    print("Invalid water usage!")
else:
    bill = calculate_charge(units)
    category = usage_category(units)
    tip = conservation_tip(category)

    print("\n------ BILL DETAILS ------")
    print("Consumer Name:", name)
    print("Total Units:", units)
    print("Final Bill Amount: Rs.", bill)
    print("Usage Category:", category)
    print("Message:", tip)
