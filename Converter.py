def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084

def km_to_meters(km):
    return km * 1000

while True:
    print("\n--- Unit Converter ---")
    print("1. Kilometers → Miles")
    print("2. Miles → Kilometers")
    print("3. Meters → Feet")
    print("4. Feet → Meters")
    print("5. Kilometers → Meters")
    print("0. Exit")

    choice = input("Choose an option: ")

    if choice == "0":
        print("Goodbye!")
        break

    value = float(input("Enter value to convert: "))

    if choice == "1":
        print(f"{value} km = {km_to_miles(value):.3f} miles")
    elif choice == "2":
        print(f"{value} miles = {miles_to_km(value):.3f} km")
    elif choice == "3":
        print(f"{value} meters = {meters_to_feet(value):.3f} feet")
    elif choice == "4":
        print(f"{value} feet = {feet_to_meters(value):.3f} meters")
    elif choice == "5":
        print(f"{value} km = {km_to_meters(value):.3f} meters")
    else:
        print("Invalid option, try again.")
