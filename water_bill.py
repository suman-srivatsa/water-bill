def calculate_charge(units):
    charge = units * 7
    service_charge = 30

    if units > 30:
        service_charge = 60
    elif units > 15:
        service_charge = 45

    return charge + service_charge


def usage_category(units):
    if units <= 15:
        return "Low Usage"
    elif units <= 30:
        return "Medium Usage"
    else:
        return "Excessive Usage"


def conservation_tip(category):
    if category == "Low Usage":
        return "Excellent! Maintain your water-saving habits."
    elif category == "Medium Usage":
        return "Try reducing daily water consumption."
    else:
        return "Reduce water usage and check for leakage."


print("     WATER BILL MANAGEMENT SYSTEM")

name = input("Enter Consumer Name: ")
units = float(input("Enter Water Usage: "))

if units < 0:
    print("Invalid water usage!")
else:
    bill = calculate_charge(units)
    category = usage_category(units)
    tip = conservation_tip(category)

    print("\n------ WATER BILL ------")
    print("Consumer Name:", name)
    print("Water Usage:", units, "units")
    print("Total Water Bill: Rs.", bill)
    print("Usage Category:", category)
    print("Conservation Tip:", tip)
