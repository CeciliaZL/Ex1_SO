def pEstatica():
    while True:
        noParticiones = int(input ('Ingrese el número de particiones que desea tener, no mayor a 10'))
        if (noParticiones <=10):
            print('vfgt')
    else:
         print ('Está solicitando más de las particioenes que se peuden hacer')
        
	# datos = []:
	# while particiones = num:
		

def pDinamica():
	print('dinamico')

def pPaginacion():
	print('paginacion')

def pSegmentacion():
	print('segmentacion')
        

def menu():
    while True:
        print("\n\t\t\t------Huitzilix-------\n")
        print("Zurita León Dana Cecilia\n\n\n")
        print("Caracteristicas de dispositivo\n\n")
        print("Memoria 2048 MB")
        print("Memoria base 640 KB")
        print("Sistema operativo 384 KB")
        print("Mmeoria para aplicaciones 1024 KB")
        print("¿Qué gestion de memoria le gustaria implementar?: ")
        print("1. Particionamiento estatico")
        print("2. Particionamiento Dinamico")
        print("3. Particionamiento por pagianción")
        print("4. Particionamiento por segmentación")
        print("5. Salir")
        print

        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            pEstatica()
            
            pass
        elif opcion == "2":
            pDinamica()
            
            pass
        elif opcion == "3":
            pPaginacion()
            
            pass
        elif opcion == "4":
            pSegmentacion()
            pass
        elif opcion == "5":
            break
            print("¡Hasta luego!")
        else:
            print("Opción inválida")

menu()