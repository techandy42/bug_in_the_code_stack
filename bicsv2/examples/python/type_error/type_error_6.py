def celsius_to_fahrenheit():
    celsius = input("Enter temperature in Celsius: ")
    try:
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit
    except ValueError:
        return "Invalid input. Please enter a number."
    