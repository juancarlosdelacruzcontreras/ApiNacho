#Dianaromero 19/01/2021#
ciclo = True

while ciclo == True:
    try:
        menu = int(input("Seleccionar API: \n 1.- Usar ipstack \n 2.- Usar ipapi \n 0.- Salir \n"))

        if menu == 1:
            try:
                ip = int(input("Seleccionar tipo de dirección: \n 1.- IPv4 \n 2.- IPv6"))

                if ip == 1:
                    print("ipstack con IPv4")
                    
                elif ip == 2:
                    print("ipstack con IPv6")

                else:
                    print("Ingresa un número que aparezca en la lista")
                    
            except ValueError:
                print("")
                
        elif menu == 2:
            try:
                ip = int(input("Seleccionar tipo de dirección: \n 1.- IPv4 \n 2.- IPv6"))

                if ip == 1:
                    print("ipapi con IPv4")
                    
                elif ip == 2:
                    print("ipapi con IPv6")

                else:
                    print("Ingresa un número que aparezca en la lista")
                    
            except ValueError:
                print("Ingresa sólo números enteros")
                
        elif menu == 0:
            break
            ciclo = True

        else:
            print("Ingresa un número que aparezca en la lista")

    except ValueError:
        print("")
        ciclo = True
