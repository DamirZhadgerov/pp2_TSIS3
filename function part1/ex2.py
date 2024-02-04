def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius

# Read the temperature in Fahrenheit from the user
fahrenheit = float(input("Enter the temperature in Fahrenheit: "))

# Convert Fahrenheit to Celsius
celsius = fahrenheit_to_celsius(fahrenheit)

# Display the result
print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius:.2f} degrees Celsius.")
