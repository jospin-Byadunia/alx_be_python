FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit-32)*FAHRENHEIT_TO_CELSIUS_FACTOR

def  convert_to_fahrenheit(celsius):
    return (celsius*CELSIUS_TO_FAHRENHEIT_FACTOR)+32

temp_value = float(input("Enter the temperature to convert: "))
temp = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
if not temp_value:
    print("Invalid temperature. Please enter a numeric value.")
else:
    match temp:
        case 'C':
            print(f"{temp_value}°C is {convert_to_fahrenheit(temp_value)}°F")
        case 'F':
            print(f"{temp_value}°F is {convert_to_fahrenheit(temp_value)}°C")
        case _:
            print("")