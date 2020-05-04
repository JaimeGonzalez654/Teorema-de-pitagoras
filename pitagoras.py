import math
print("Teorema de pitagoras")
print("Introduzca los datos porfavor")
print("Introduzca el cateto 1 (coloque 0 si es el dato que busca)")
cateto_1 = float(input())
print("Introduzca el cateto 2 (coloque 0 si es el dato que busca)")
cateto_2 = float(input())
print("Introduzca la hipotenusa (coloque 0 si es el dato que busca)")
hipotenusa = float(input())
print("¿Que desea obtener?")
print("=======================================================================")
print("cateto_1 (presione 1)")
print("cateto_2 (presione 2)")
print("Hipotenusa (presione 3)")
print("=======================================================================")
opcion = float(input())
if opcion == 1:
    Cateto_1 = ((hipotenusa ** 2) - (cateto_2 ** 2))
    print("El cateto 1 corresponde a ", math.sqrt(Cateto_1))
 
elif opcion == 2:
    Cateto_2 = ((hipotenusa ** 2) - (cateto_1 ** 2))
    print("El cateto 2 corresponde a ", math.sqrt(Cateto_2))
    
elif opcion == 3:
    Hipotenusa = ((cateto_1 ** 2) + (cateto_2 ** 2))
    print("La hipotenusa corresponde a ", math.sqrt(Hipotenusa))
 
else:
    print("La operacion no se pudo realizar")
 







