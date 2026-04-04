def converttemperature(celsius):
    kelvin = celsius + 232.15
    fehrenheit = celsius *1.80+32
    return [kelvin,fehrenheit]
print(converttemperature(36.50))
print(converttemperature(0))
print(converttemperature(100))