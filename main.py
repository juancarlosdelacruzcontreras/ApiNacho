#Dianaromero 19/01/2021
#JoseAngelHerrera 24/07/2021
from progress.bar import Bar, ChargingBar
import modelips as nin
import modelipa as dani
import os, time, random
from tabulate import tabulate
from colorama import Fore, init, Style, Back
init()


ciclo = True
while ciclo == True:
    try:
        print(Fore.GREEN + "CONSUMO DE APIS")
        print(Fore.YELLOW + "APIS: \n 1.- Usar ipstack \n 2.- Usar ipapi \n 0.- Salir") 

        print(Fore.WHITE + " ")
        menu = int(input("Seleccionar API: "))

        if menu == 1:
            try:
                print(" ")
                print(Fore.GREEN + "SELECCION DE DIRECCIONES")
                print(Fore.YELLOW + "Tipo de dirección: \n 1.- IPv4 \n 2.- IPv6") 
            
                print(Fore.WHITE + " ")
                op = int(input("Seleccionar tipo de dirección: "))

                if op == 1:
                    response = nin.ipstack_info()
                    items=response.items()
                    mylist=list(items)

                    print(" ")
                    bar2 = ChargingBar('Obteniendo informacion:', max=100)
                    for num in range(100):
                        time.sleep(random.uniform(0, 0.2))
                        bar2.next()
                    bar2.finish()
                    print(" ")
                    
                    print(Fore.GREEN + "Tabla de resultados desde IPSTACK")
                    print(Style.RESET_ALL + Fore.CYAN + tabulate(mylist, tablefmt='plain'))
                    print(" ")

                    
                elif op == 2:
                    response = nin.ipstack_info()
                    items=response.items()
                    mylist=list(items)

                    print(" ")
                    bar2 = ChargingBar('Obteniendo informacion:', max=100)
                    for num in range(100):
                        time.sleep(random.uniform(0, 0.2))
                        bar2.next()
                    bar2.finish()
                    print(" ")
                    
                    print(Fore.GREEN + "Tabla de resultados desde IPSTACK")
                    print(Style.RESET_ALL + Fore.CYAN + tabulate(mylist, tablefmt='plain'))
                    print(" ")

                else:
                    print(" ")
                    print(Style.RESET_ALL + Fore.RED + "Lo sentimos no contamos con esa opcion :c")
                    print(" ")
                    
            except ValueError:
                print (" ")
                print(Style.RESET_ALL + Fore.RED + "!Numero invalido!")
                print(" ")

        #Ricardo 23/07/2021        
        elif menu == 2:
            try:
                print(" ")
                print(Fore.GREEN + "SELECCION DE DIRECCIONES")
                print(Fore.YELLOW + "Tipo de dirección: \n 1.- IPv4 \n 2.- IPv6")
                
                print(Fore.WHITE + " ")
                op = int(input("Seleccionar tipo de dirección: "))
                

                if op == 1:
                    response = dani.ipapi_info()
                    items=response.items()
                    mylist=list(items)

                    print(" ")
                    bar2 = ChargingBar('Obteniendo informacion:', max=100)
                    for num in range(100):
                        time.sleep(random.uniform(0, 0.2))
                        bar2.next()
                    bar2.finish()
                    print(" ")
                    
                    print(Fore.GREEN + "Tabla de resultados desde IPAPI")
                    print(Style.RESET_ALL + Fore.CYAN + tabulate(mylist, tablefmt='plain'))
                    print(" ")
                    
                elif op == 2:
                    response = dani.ipapi_info()
                    items=response.items()
                    mylist=list(items)

                    print(" ")
                    bar2 = ChargingBar('Obteniendo informacion:', max=100)
                    for num in range(100):
                        time.sleep(random.uniform(0, 0.2))
                        bar2.next()
                    bar2.finish()
                    print(" ")
                    
                    print(Fore.GREEN + "Tabla de resultados desde IPAPI")
                    print(Style.RESET_ALL + Fore.CYAN + tabulate(mylist, tablefmt='plain'))
                    print(" ")

                else:
                    print(" ")
                    print(Style.RESET_ALL + Fore.RED + "Lo sentimos no contamos con esa opcion :c")
                    print(" ")
                    
            except ValueError:
                print (" ")
                print(Style.RESET_ALL + Fore.RED + "!Numero invalido!")
                print(" ")
                
        elif menu == 0:
            print(" ")
            print (Style.RESET_ALL + Fore.CYAN + "################################################")
            print(Style.RESET_ALL + Fore.CYAN + "GRACIAS POR SU PREFERENCIA, NOS VEMOS PRONTO :P")
            print ("################################################")
            break

        else:
            print(" ")
            print(Style.RESET_ALL + Fore.RED + "Ingresa un número que aparezca en la lista")
            print(" ")

    except ValueError:
        print(" ")
        print(Style.RESET_ALL + Fore.RED + "Caracter invalido")
        print("")
        ciclo = True

