

#Datos que se usaran para las particiones  
def datos():
     memoriaT = 2048
     memoriaB = 640
     memoriaSO = 384
     memoriaApps = 1024

def pEstatica():

    print("--------------------------------------")
    print("\n\tPartición estática")
    particion = int(input("ingrese el númeor de partiones que requiere\n\n"))
    
    if particion <=10: {
        print("jasas")        
    }
    else: 
         print("Solicita más de las particiones permitidas")
    
    
    
    
    
    
    
    """while True:
        noParticiones = int(input ('Ingrese el número de particiones que desea tener, no mayor a 10'))
        if (noParticiones <=10):
            print('vfgt')
    else:
         print ('Está solicitando más de las particioenes que se peuden hacer')
       """ 

		

def pDinamica():
	print('dinamico')

def pPaginacion():
	print('paginacion')

def pSegmentacion():
	print('segmentacion')
        
# Definir menu
def main(pEstatica):
    while True:
        print("\n\n\n\t\t------  Huitzilix  -------\n")
        print("\tZurita León Dana Cecilia\n\n")
        print("\tCaracteristicas de dispositivo\n")
        print("\tMemoria 2048 MB")
        print("\tMemoria base 640 KB")
        print("\tSistema operativo 384 KB")
        print("\tMmeoria para aplicaciones 1024 KB\n\n")
        
        print("\t\t¿Qué gestión de memória le gustaría implementar?: \n")
        
        print("\t1. Particionamiento estatico")
        print("\t2. Particionamiento Dinamico")
        print("\t3. Particionamiento por pagianción")
        print("\t4. Particionamiento por segmentación")
        print("\t5. Salir\n")

        opcion = input("\nIngrese su opción: \n")
        if opcion == "1":
            print("h")
            pEstatica()

        elif opcion == "2":
            print("2")
            # pDinamica()
        elif opcion == "3":
            print("3")
            # paginacion()
        elif opcion == "4":
            print("4")
            # segmentacion()
        elif opcion == "5":
            print("Salio del programa\n")
            break
        else:
            print("\nOpción invalida")

main(pEstatica)