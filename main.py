actualTemp = 75
desiredTemp = 70

if actualTemp > desiredTemp:
    print("Run A/C")
elif actualTemp < desiredTemp:
    print("Run heat")
else:
    print("Standby")


tempStr = input('Enter the temperature in Celsius: ')
tempCelsius = float(tempStr)
targetUnit = input('What unit would you like this converted to? (C/F/K): ')

if targetUnit == "C":
    convertedTemp = tempCelsius
elif targetUnit == "F":
    convertedTemp = (tempCelsius * 9/5) + 32
elif targetUnit == "K":
    convertedTemp = tempCelsius + 273.15
else:
    print("Invalid target unit. Please choose 'C', 'F', or 'K'.")
    convertedTemp = None

if convertedTemp is not None:
    print(f"The temperature is {convertedTemp} {targetUnit}.")
    print(f"You entered {tempCelsius} Celsius.")
