from django.http import HttpResponse

def saludo(request): #primera vista
    #Declaracion de variables
    int_Edad = 0
    float_Estatura = 0.0
    str_Inicial =""
    str_Apellido =""

    #Inicio del programa
    int_Edad = int (input("Introduce tu edad: "))
    float_Estatura = float (input("Introduce tu estatura: "))
    str_Inicial = (input("Introduce tu nombre: "))
    str_Apellido = (input("Introduce tu apellido: "))


    return HttpResponse(f"Hello word! Soy {str_Inicial} {str_Apellido}. Tengo {int_Edad} y mido {float_Estatura}")

def despedida(request):
    return HttpResponse("")

def facturas(request):
    srt_Trama = "2500000777" #6E+3D = 2500000.777
    int_Parte_Entera = 0 #6E
    int_Parte_Decimal = 0 #3D

    print("***** FORMATEAR TRAMA *****")
    print("")
    print("***************************")
    print("Trama inicial: %s"%(srt_Trama))
    print("***************************")
    print("")
    int_Parte_Entera = int(srt_Trama)/1000
    print("Parte entera (6E) : %d " %(int_Parte_Entera))
    int_Parte_Decimal = int(srt_Trama) % 1000
    print("Parte decimal (3D) : %d " % (int_Parte_Decimal))
    print("")
    print("***************************")
    print("Precio (6D+3D) : %d.%d" % (int_Parte_Entera,int_Parte_Decimal))
    print("***************************")
    return HttpResponse("Precio (6D+3D) : %d.%d" % (int_Parte_Entera,int_Parte_Decimal))

def ejercicio1(request):
    #Área cuadrado
    print("Area de un cuadrado<br> ")
    float_Lado = float (input("Introduce el lado en cm: "))
    float_Area_Cuadrado = float_Lado ** 2

    #Área triangulo
    print("Area de un triangulo:<br>")
    float_Base = float (input("Introduce la base en cm: "))
    float_Altura_T = float (input("Introduce la altura en cm: "))
    float_Area_Triangulo = (float_Base*float_Altura_T)/2
    
    #Área circulo
    print("Area de un circulo:<br>")
    const_PI = 3.18
    float_radio = float (input("Introduce el radio en cm: "))
    float_Area_Circulo = const_PI * (float_radio ** 2)

    #Grados Farenheit a celcius

    float_faren = float(input("Indica los grados en Farenheit: "))    
    float_Celsius = ((float_faren - 32.0) * 5.0) / 9.0
    return HttpResponse(f"Según los datos introducidos:<br>área del cuadrado es {float_Area_Cuadrado}.<br>El área del triangulo es {float_Area_Triangulo}.<br>El area del circulo es {float_Area_Circulo}.<br> Los grados celsuius son: {float_Celsius}")

def reto1(request):
    str_Precio1 = "11111111"
    str_Precio2 = "22222222"
    str_Precio3 = "33333333"
    str_Precio4 = "44444444"
    int_Total = int(str_Precio1) + int(str_Precio2) + int(str_Precio3) + int(str_Precio4) 
    int_Parte_Entera = int_Total / 1000 
    int_Parte_Decimal = int_Total % 1000 
    return HttpResponse("El precio total es: %d.%d" % (int_Parte_Entera,int_Parte_Decimal))