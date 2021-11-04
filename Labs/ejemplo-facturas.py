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