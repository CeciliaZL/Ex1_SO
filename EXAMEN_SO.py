#Datos que se usaran para las particiones  
def datos():
     memoriaT = 2048
     memoriaB = 640
     memoriaSO = 384
     memoriaApps = 1024

def pEstatica():

    print("--------------------------------------")
    print("\n\tPartición estática")
    particion = int(input("\tIngrese el número de partiones que requiere\n\n"))
    memoriaApps =1024
    a = 0 

    if (particion <=10):
        for i in range(0,particion-1):
            print("\tPartición ", i +1)
            valPart = int(input("\tTamaño: ")) 
            if (valPart<=memoriaApps):
                a = a + valPart
                print("aoaoaao: ", a)        
                print("La suma es ", a)
                
            else:
                print("El tamaño de la particion es mayo al de la memoria")
                break
            
    
    else: 
         print("Solicita más de las particiones permitidas")

    







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