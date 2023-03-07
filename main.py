def heating_cooling(actualTemp, desiredTemp):
    if actualTemp > desiredTemp:
        return "Run A/C"
    elif actualTemp < desiredTemp:
        return "Run heat"
    else:
        return "Standby"

actualTemp = input('What is the actual temp? ')
desiredTemp = input('What is the desired temp? ')
print(heating_cooling(actualTemp,desiredTemp))


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
