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


def celsius_conversion(tempCelsius, targetUnit):
    # Check the target unit and convert the temperature accordingly
    if targetUnit == 'C':
        converted_temp = tempCelsius
    elif targetUnit == 'F':
        converted_temp = (tempCelsius * 9/5) + 32
    elif targetUnit == 'K':
        converted_temp = tempCelsius + 273.15
    else:
        return 'Invalid target unit. Please choose (C/F/K).'

    return f'{converted_temp:.1f} {targetUnit}'




tempStr = input('Enter the temperature in Celsius: ')
tempCelsius = float(tempStr)
targetUnit = input('What unit would you like this converted to? (C/F/K): ')
print(celsius_conversion(tempCelsius,targetUnit))

