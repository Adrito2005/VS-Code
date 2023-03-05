a = int(input("Enter the temperature (magnitude only) "))
b = input("Enter the unit of the temperature entered ")

b = b.upper()

if (b == 'F'):
    x = ((a-32)*5)/9
    print("Converted to Celsius Temperature is ", x, "°C")
elif (b == 'C'):
    x = ((a*9)/5)+32
    print("Converted to Ferhenite Temperature is ", x, "°F")
else:
    print("invalid unit")
