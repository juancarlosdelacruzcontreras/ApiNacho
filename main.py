#Dianaromero 19/01/2021
import modelips as nin
import modelipa as dani
import os

ciclo = True

while ciclo == True:
    try:
        print("APIS: \n 1.- Usar ipstack \n 2.- Usar ipapi \n 0.- Salir")
        menu = int(input("Seleccionar API: "))

        if menu == 1:
            try:
                print("Tipo de dirección: \n 1.- IPv4 \n 2.- IPv6")
                op = int(input("Seleccionar tipo de dirección: "))

                if op == 1:
                    response = nin.ipstack_info()
                    print(response)
                    
                elif op == 2:
                    response = nin.ipstack_info()
                    print(response)

                else:
                    print("Ingresa un número que aparezca en la lista")
                    print("")
                    
            except ValueError:
                print("Ingresa sólo números enteros")
                print("")

        #Ricardo 23/07/2021        
        elif menu == 2:
            try:
                print("Tipo de dirección: \n 1.- IPv4 \n 2.- IPv6")
                op = int(input("Seleccionar tipo de dirección: "))

                if op == 1:
                    response = dani.ipapi_info()
                    print(response)
                    
                elif op == 2:
                    response = dani.ipapi_info()
                    print(response)

                else:
                    print("Ingresa un número que aparezca en la lista")
                    print("")
                    
            except ValueError:
                print("Ingresa sólo números enteros")
                print("")
                
        elif menu == 0:
            print("Adios")
            break

        else:
            print("Ingresa un número que aparezca en la lista")

    except ValueError:
        print("Caracter invalido")
        print("")
        ciclo = True
