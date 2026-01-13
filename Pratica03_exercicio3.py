#3- Conversor de Temperatura
#Crie um programa que converta temperaturas entre:
#Celsius, Fahrenheit e Kelvin.
#O usuário deve informar a temperatura, 
# a unidade de origem e a unidade para qual deseja converter.

temperatura = int(input("Informe a Temperatura atual: "))
unidadedeorigem = input("Informe a unidade de origem: ")
unidadededestino = input("Informe a unidade para qual deseja converter: ")



convertcelsius_kelvin = (temperatura + 273.15)
convertkelvin_celsius =  (temperatura - 273.15)
convertcelsius_fahrenheit = (temperatura * 9/5) + 32
convertfahrenheit_celsius = (temperatura - 32) * 5/9
convertkelvin_fahrenheit = (temperatura - 273.15) * 9/5 + 32
convertfahrenheit_kelvin = (temperatura - 32) * 5/9 + 273.15

if unidadedeorigem == "C" and unidadededestino == "K":
    print(f"{convertcelsius_kelvin:.2f} °K")

if unidadedeorigem == "K" and unidadededestino == "C": 
    print(f"{convertkelvin_celsius:.2f} ° C")

if unidadedeorigem == "C" and unidadededestino == "F":
    print(f"{convertcelsius_fahrenheit:.2f} ° F")

if unidadedeorigem == "F" and unidadededestino == "C":
    print(f"{convertfahrenheit_celsius:.2f} ° C")

if unidadedeorigem == "K" and unidadededestino == "F":
    print(f"{convertkelvin_fahrenheit:.2f} ° F")

if unidadedeorigem == "F" and unidadededestino == "K":
    print(f"{convertfahrenheit_kelvin:.2f} ° K")
