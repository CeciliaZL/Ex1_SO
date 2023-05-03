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
                print("Ordenado ", vProceso) 
            else:
                print("\n\tMemoria insufucuente")        
    else: 
        print("\n\tSolicita más de las particiones permitidas")


#----------------------------------------------------------------------------------------------------------------------------------------------------------------

def pDinamica():
    memoriaT =2048
    rest = 0
    print("--------------------------------------")
    print("\n\tPartición Dinámica")

#------------------------------------FALIDAR QUE CUANDO SEA INSUFICIENTE SE SALGA --------------
    while True:
        procesoD = int(input("\tIngrese el tamaño del proceso: "))
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

    print("Puede dividir la memoria con 2KB, 4KB u 8KB")
    paginar  = int(input("Ingrese el número de particiones: "))

    if (paginar == 2) or (paginar == 4) or (paginar == 8):
        for i in range (0, memoriaT<=0): 
            div =  memoriaT // paginar
            division.append(div)
            print ("La capacidad por segmento es de: ", div, "KB")
            pros  = int(input("Tamaño del proceso: ")) 
            div2 = pros // paginar
            div1.append(div2)
            print("DIVISION 1 ", div1)


            resta =  div - div2
            restas.append(resta)
            print (" RESTA 1 ", restas)

            for i in range (0, resta >=0):
                pros  = int(input("Tamaño del proceso: ")) 
                div2 = pros // paginar
                div1.append(div2)
                print ("HOLA   ", div1)
                resta =  div - div2
                restas.append(resta)
                print ("Resta es ", restas)
        


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
            pPaginacion()

        elif opcion == "4":
            print("4")
            # segmentacion()
        elif opcion == "5":
            print("Salio del programa\n")
            break
        else:
            print("\nOpción invalida")

main(pEstatica)