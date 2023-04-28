#Datos que se usaran para las particiones  


import numpy as np

def datos():
     memoriaT = 2048
     memoriaB = 640
     memoriaSO = 384
     memoriaApps = 1024

def pEstatica():

    valores = []
    vProceso = []
    print("--------------------------------------")
    print("\n\tPartición estática\n")

    print("\tLa cantidad maxima de particiones son 10")
    particion = int(input("\tIngrese el número de partiones que requiere: "))
    memoriaApps =1024
    a = 0 
    b = []
    o = 0
#--------------------------------  No tiene que salir particion final si se sale en el if pasado  ---------------------------------
    if (particion <=10):

        #---------------Validacion para que la ultima de cero o si ya tiene los 1024 no deje

        for i in range(0,particion-1):
            print("\n\tPartición ", i +1)
            valPart = int(input("\tTamaño: ")) 
            valores.append(valPart)
            if (valPart<=memoriaApps):
                a = a + valPart      
            else:
                print("El tamaño de la particion es mayor al de la memoria")
                break
        if (a <= memoriaApps):    
            b = memoriaApps - a
            print("\n\tPartición ", particion)  
            print ("\tTamaño: ", b)
            vPart= np.append(valores, b)
            vPart.sort()
            print("El valor de x es ",vPart)
            
            for j in range (0, particion ):
                print("\n\tProceso ", j + 1 )
                proceso = int(input("\tTamaño: "))
                vProceso.append(proceso)
                vProceso.sort()
            print("Ordenado ", vProceso)

            for l in range (0, particion):
                if (vProceso[l]<=vPart[l]):
                    print("El proceso de ", vProceso[l], "kb se ha asignado a la partición de", vPart[l], "kb")     
                else:
                    print("El proceso de ", vProceso[l], " KB no se pudo asignar a ninguna partición ")
        else:
            print("no se puede ingresar esa partición")
        
    else: 
        print("Solicita más de las particiones permitidas")


#----------------------------------------------------------------------------------------------------------------------------------------------------------------

def pDinamica():
    memoriaApps =1024
    tamDin = []
    restaT = 0
    print("--------------------------------------")
    print("\n\tPartición Dinámica")


    procesoD = int(input("\tIngrese el tamaño del proceso\n\n"))
    tamDin.append(procesoD)
    
    if (procesoD <= memoriaApps):
        memoriaApps -= procesoD                
    else:
        print("Excedes el tamaño de la memoria disponible")
        
            
            


    
         



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
            pDinamica()
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