#Datos que se usaran para las particiones  


import numpy as np

def datos():
     memoriaT = 2048
     memoriaB = 640
     memoriaSO = 384
     memoriaApps = 1024

def pEstatica():

    memoriaApps =1024
    a = 0 
    b = []
    valores = []
    vProceso = []


    print("--------------------------------------")
    print("\n\tPartición estática\n")

    print("\tLa cantidad maxima de particiones son 10")
    particion = int(input("\tIngrese el número de partiones que requiere: "))
    
    if (particion <=10):
        for i in range(0,particion-1):
            print("\n\tPartición ", i +1)
            valPart = int(input("\tTamaño: ")) 
            valores.append(valPart)
            if (valPart<=memoriaApps):
                a = a + valPart      
            else:
                print("El tamaño de la particion es mayor al de la memoria")
                break
        if (valPart<=memoriaApps):
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
                    if (vProceso[j] <= vPart[j]):
                        print ("SALUDOS ", vProceso)
                        vProceso.sort()
                    else:
                        print("ERROR")
                        break
                for l in range (0, particion):
                    if (vProceso[j]<=vPart[j]):
                        print("\n\tEl proceso de ", vProceso[l], "KB se ha asignado a la partición de", vPart[l], "KB")     
                if (vProceso[j]>vPart[j]):
                        print("\n\tEl proceso de ", vProceso[j], " KB no se pudo asignar a ninguna partición ")
                #print("Ordenado ", vProceso) 
            else:
                print("\n\tMemoria insufucuente")        
    else: 
        print("\n\tSolicita más de las particiones permitidas")


def pDinamica():
    memoriaT =2048
    rest = 0
    print("--------------------------------------")
    print("\n\tPartición Dinámica")

    while True:
        procesoD = int(input("\n\tIngrese el tamaño del proceso: "))
        memoriaT = memoriaT - procesoD
        if (memoriaT >= 0):
            print ("\n\tTiene ", memoriaT, " KB de memoria disponible.")
        else: 
            print("\n\tMemoria insuficiente ")  
            break        

def pPaginacion():
    
    print("--------------------------------------")
    print("\n\tPaginación")
    memoriaT = 1024
    resta = 0
    div1= []
    restas = []
    division =[]

    print("\tPuede dividir la memoria con 2KB, 4KB u 8KB")
    paginar  = int(input("\tIngrese el tamaño del marco: "))

    if (paginar == 2) or (paginar == 4) or (paginar == 8):
        div =  memoriaT // paginar
        
        while True: 
  
            print ("\n\tMarcos disponibles: ", div, "KB")
            pros  = int(input("\tTamaño del proceso: ")) 
            div2 = pros // paginar
            div -= div2
            if(div<=0):
                print("\n\tMemoria insuficiente")
                break
           

def pSegmentacion():
    print('\n\tSegmentacion')
    memoriaT = 2048
    rest = 0
    print("--------------------------------------")
    print("\n\tPartición Dinámica")

    while True:
        procesoD = int(input("\n\tIngrese el tamaño del proceso: "))
        memoriaT = memoriaT - procesoD
        if (memoriaT >= 0):
            sc = procesoD * 0.1
            sd = procesoD * 0.5
            sp = procesoD * 0.4
            suma = sc + sd + sp
            print ("\n\tSegmentación Código: ", sc)
            print ("\n\tSegmentación Datos: ", sd)
            print ("\n\tSegmentación Pila: ", sp)
            print ("\n\tTotal de segmetación ", suma)
            print ("\n\tTiene ", memoriaT, " KB de memoria disponible.")
        else: 
            print("\n\tMemoria insuficiente ")  
            break  
        
        
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

        opcion = input("\n\tIngrese su opción: \n")
        if opcion == "1":
            pEstatica()

        elif opcion == "2":
            pDinamica()
            
        elif opcion == "3":
            pPaginacion()

        elif opcion == "4":
            pSegmentacion()

        elif opcion == "5":
            print ("-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ")
            print("\n\tSalio del programa\n")
            break
        else:
            print("\n\tOpción invalida")

main(pEstatica)