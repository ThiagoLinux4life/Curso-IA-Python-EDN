#3- Conversor de Temperatura
#Crie um programa que converta temperaturas entre:
#Celsius, Fahrenheit e Kelvin.
#O usuário deve informar a temperatura, 
# a unidade de origem e a unidade para qual deseja converter.

temperatura = int(input("Entre com a Temperatura atual: "))

convertcelsius_kelvin = (temperatura + 273.15)
convertkelvin_celsius =  (temperatura - 273.15)
convertcelsius_fahrenheit = (temperatura * 9/5) + 32
convertfahrenheit_celsius = (temperatura - 32) * 5/9
convertkelvin_fahrenheit = (temperatura - 273.15) * 9/5 + 32
convertfahrenheit_kelvin = (temperatura - 32) * 5/9 + 273.15

if convertcelsius_kelvin:
    print(f"{convertcelsius_kelvin:.2f} °K")

if convertkelvin_celsius:
    print(f"{convertkelvin_celsius:.2f} ° C")

if convertcelsius_fahrenheit:
    print(f"{convertcelsius_fahrenheit:.2f} ° F")

if convertfahrenheit_celsius:
    print(f"{convertfahrenheit_celsius:.2f} ° C")

if convertkelvin_fahrenheit:
    print(f"{convertkelvin_fahrenheit:.2f} ° F")

if convertfahrenheit_kelvin:
    print(f"{convertfahrenheit_kelvin:.2f} ° K")
