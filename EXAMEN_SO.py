#Datos que se usaran para las particiones  


import numpy as np

def datos():
     memoriaT = 2048
     memoriaB = 640
     memoriaSO = 384
     memoriaApps = 1024

def pEstatica():

    valores = []
    print("--------------------------------------")
    print("\n\tPartición estática")
    particion = int(input("\tIngrese el número de partiones que requiere\n\n"))
    memoriaApps =1024
    a = 0 
    b = []
    o = 0

########################   No tiene que salir particion final si se sale en el if pasado  #############################################


    if (particion <=10):
        for i in range(0,particion-1):
            print("\n\tPartición ", i +1)
            valPart = int(input("\tTamaño: ")) 
            valores.append(valPart)
            #valores.sort()

            
            if (valPart<=memoriaApps):
                a = a + valPart
                              
            else:
                print("El tamaño de la particion es mayor al de la memoria")
                break
        b = memoriaApps - a
        print("\tPartición ", particion)  
        print ("\tTamaño: ", b)
        ##################Puedo meter una suma para hacer una lista anidad<
        #o = a+b  
        #print("\nLa suma es ", o)
        print("El valor de las particiones son ", particion)
        vFinal = np.append(valores, b)
        print("El valor de x es ",vFinal)

        for j in range (0, particion ):
            print("\n\tProceso ", j + 1 )
            proceso = int(input("\tTamaño: "))

    
    else: 
         print("Solicita más de las particiones permitidas")



###############################################################################################################################################333














def pDinamica():

    print("--------------------------------------")
    print("\n\tPartición Dinámica")
    particion = int(input("\tIngrese el número de partiones que requiere\n\n"))
    memoriaApps =1024
    procesos = 0
    a = 0 
    b = 0

    if (particion <=10):
        for i in range(0,particion-1):
            print("\tPartición ", i +1)
            valPart = int(input("\tTamaño: ")) 
            if (valPart<=memoriaApps):
                a = a + valPart
                              
            else:
                print("El tamaño de la particion es mayo al de la memoria")
                break
        b = memoriaApps - a
        print("Partición ", 1 + i, "es: ",b)   
        print("La suma es ", a)             
    
    else: 
         print("Solicita más de las particiones permitidas")

    procesos = particion
    for p in range (0, procesos):
        procesos = int(input("\n\n\tIngres el proceso ", p + 1))
        #if (procesos <= valPart):

         



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