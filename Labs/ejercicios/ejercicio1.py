 #Área cuadrado
print("Area de un cuadrado")
float_Lado = float (input("Introduce el lado en cm: "))
float_Area_Cuadrado = float_Lado ** 2
print("El area es %d" % float_Area_Cuadrado)
print("")
#Área triangulo
print("Area de un triangulo:<br>")
float_Base = float (input("Introduce la base en cm: "))
float_Altura_T = float (input("Introduce la altura en cm: "))
float_Area_Triangulo = (float_Base*float_Altura_T)/2
print("El area es %d" % float_Area_Triangulo)
print("")
#Área circulo
print("Area de un circulo:<br>")
const_PI = 3.18
float_radio = float (input("Introduce el radio en cm: "))
float_Area_Circulo = const_PI * (float_radio ** 2)
print("El area es %d" % float_Area_Circulo)
print("")
#Grados Farenheit a celcius

float_faren = float(input("Indica los grados en Farenheit: "))    
float_Celsius = ((float_faren - 32.0) * 5.0) / 9.0
print("Se transforman en %d grados celsius" % float_Celsius)
print("")