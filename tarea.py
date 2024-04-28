agua = int(input("Introduzca la cantidad de agua en mililitros: "))
harina = int(input("Introduzca la cantidad de harina en gramos: "))
masa_arepa = 50.0 # 50 gramos para una arepa
cantidad_arepas = harina / masa_arepa
print("Con " + str(harina) + "g de harina y " + str(agua) + "ml de agua resultarán, en promedio, " + str(cantidad_arepas) + " arepas") 
