str_Precio1 = "11111111"
str_Precio2 = "22222222"
str_Precio3 = "33333333"
str_Precio4 = "44444444"
int_Total = int(str_Precio1) + int(str_Precio2) + int(str_Precio3) + int(str_Precio4) 
int_Parte_Entera = int_Total / 1000 
int_Parte_Decimal = int_Total % 1000 
print("El precio total es: %d.%d" % (int_Parte_Entera,int_Parte_Decimal))