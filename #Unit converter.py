#Unit converter
#First,we define conversion functions 
def length_convert(value,from_unit,to_unit):
    #create a dictionary to define length units
    length_units = {
        'centimeters':0.01,
        'meters':1,
        'kilometers':1000,
        'millimeters':0.001,
        'feet':0.3048,
        'inches':0.0254,
        'miles':1609.34,
        'yards':0.9144
    }
    try:
        value_in_meters = value * length_units[from_unit]
        return value_in_meters / length_units[to_unit]
    except KeyError:
        return "Invalid length units"
def weight_convert(value,from_unit,to_unit):
    #create a dictionary to define weight units
    weight_units={
        'kilograms':1,
        'grams':0.001,
        'milligrams':0.000001,
        'pounds':0.453592,
        'ounces':0.0273495
    }
    try:
        value_in_kilograms = value * weight_units[from_unit]
        return value_in_kilograms / weight_units[to_unit]
    except KeyError:
        return "Invalid weight units"
def temperature_convert(value, from_unit, to_unit):
    try:
        if from_unit == 'celsius':
            if to_unit == 'fahrenheit':
                return (value * 9/5) + 32
            elif to_unit == 'kelvin':
                return value + 273.15
        elif from_unit == 'fahrenheit':
            if to_unit == 'celsius':
                return (value - 32) * 5/9
            elif to_unit == 'kelvin':
                return (value - 32) * 5/9 + 273.15
        elif from_unit == 'kelvin':
            if to_unit == 'celsius':
                return value - 273.15
            elif to_unit == 'fahrenheit':
                return (value - 273.15) * 9/5 + 32
    except KeyError:
        return "Invalid temperature units"
#we define user interface
def show_menu():
    print("____Unit Converter____")
    print("1. Convert Length")
    print("2. Convert Weight")
    print("3. Convert Temperature")
    print("4. Exit")
    print()

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")
        print()
        
        if choice == '1':
            value = float(input("Enter the value to convert: "))
            from_unit = input("Enter the from_unit: ").lower()
            to_unit = input("Enter the to_unit: ").lower()
            result = length_convert(value, from_unit, to_unit)
            print(f"{value} {from_unit} is equal to {result} {to_unit}")
        elif choice == '2':
            value = float(input("Enter the value to convert: "))
            from_unit = input("Enter the from_unit: ").lower()
            to_unit = input("Enter the to_unit: ").lower()
            result = weight_convert(value, from_unit, to_unit)
            print(f"{value} {from_unit} is equal to {result} {to_unit}")
        elif choice == '3':
            value = float(input("Enter the value to convert: "))
            from_unit = input("Enter the from_unit: ").lower()
            to_unit = input("Enter the to_unit: ").lower()
            result = temperature_convert(value, from_unit, to_unit)
            print(f"{value} {from_unit} is equal to {result} {to_unit}")
        elif choice == '4':
            print("Exit")
            break
        else:
            print("Please choose a number between 1 and 4.")
    print()
if __name__ == "__main__":
    main()
