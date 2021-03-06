# Dianaromero 19/01/2021
# JoseAngelHerrera 24/07/2021
import modelips as nin
import modelipa as dani
import time, random, os
from progress.bar import ChargingBar
from tabulate import tabulate
from colorama import Fore, Style

while True:
    try:
        print(Fore.GREEN + "CONSUMO DE APIS")
        print(
            Fore.YELLOW
            + "APIS: \n 1.- Usar ipstack \n 2.- Usar ipapi \n 0.- Salir"
        )

        print(Fore.WHITE + " ")
        menu = int(input("Seleccionar API: "))
        ciclo = True

        if menu == 1:
            os.system("cls" if os.name == "nt" else "clear")
            while ciclo:
                try:
                    print(" ")
                    print(Fore.GREEN + "SELECCION DE DIRECCIONES")
                    print(
                        Fore.YELLOW
                        + "Tipo de dirección: \n 1.- IPv4 \n 2.- IPv6"
                    )

                    print(Fore.WHITE + " ")
                    op = int(input("Seleccionar tipo de dirección: "))

                    if op == 1:
                        os.system("cls" if os.name == "nt" else "clear")
                        ciclo = False
                        response = list(nin.ipstack_info().items())
                        print(" ")
                        if response[1][1]:
                            bar2 = ChargingBar(
                                "Obteniendo informacion:", max=100
                            )
                            for num in range(100):
                                time.sleep(random.uniform(0, 0.001))
                                bar2.next()
                            bar2.finish()
                            print(" ")

                            print(
                                Fore.GREEN
                                + "Tabla de resultados desde IPSTACK"
                            )

                            response.append(
                                ("capital", response[12][1]["capital"])
                            )
                            response.append(
                                (
                                    "language",
                                    response[12][1]["languages"][0]["native"],
                                )
                            )
                            response.pop(12)

                            print(
                                Style.RESET_ALL
                                + Fore.CYAN
                                + tabulate(response, tablefmt="fancy_grid")
                            )
                            print("")
                        else:
                            print(
                                f"{Fore.RED}Parece que la IP introducida es una IP Privada. Inténtelo de nuevo con una IP Pública.{Style.RESET_ALL}"
                            )
                    elif op == 2:
                        os.system("cls" if os.name == "nt" else "clear")
                        ciclo = False
                        response = list(nin.ipstack_info().items())

                        print(" ")
                        bar2 = ChargingBar("Obteniendo informacion:", max=100)
                        for num in range(100):
                            time.sleep(random.uniform(0, 0.001))
                            bar2.next()
                        bar2.finish()
                        print(" ")

                        print(Fore.GREEN + "Tabla de resultados desde IPSTACK")

                        response.append(
                            ("capital", response[12][1]["capital"])
                        )
                        response.append(
                            (
                                "language",
                                response[12][1]["languages"][0]["native"],
                            )
                        )
                        response.pop(12)

                        print(
                            Style.RESET_ALL
                            + Fore.CYAN
                            + tabulate(response, tablefmt="fancy_grid")
                        )
                        print(" ")

                    else:
                        print(" ")
                        print(
                            Style.RESET_ALL
                            + Fore.RED
                            + "Lo sentimos no contamos con esa opcion :c"
                        )
                        print(" ")

                except ValueError:
                    print(" ")
                    print(Style.RESET_ALL + Fore.RED + "!Numero invalido!")
                    print(" ")

        # Ricardo 23/07/2021
        elif menu == 2:
            os.system("cls" if os.name == "nt" else "clear")
            while ciclo:
                try:
                    print(" ")
                    print(Fore.GREEN + "SELECCION DE DIRECCIONES")
                    print(
                        Fore.YELLOW
                        + "Tipo de dirección: \n 1.- IPv4 \n 2.- IPv6"
                    )

                    print(Fore.WHITE + " ")
                    op = int(input("Seleccionar tipo de dirección: "))

                    if op == 1:
                        os.system("cls" if os.name == "nt" else "clear")
                        ciclo = False
                        response = list(dani.ipapi_info().items())

                        print(" ")
                        bar2 = ChargingBar("Obteniendo informacion:", max=100)
                        for num in range(100):
                            time.sleep(random.uniform(0, 0.001))
                            bar2.next()
                        bar2.finish()
                        print(" ")

                        print(Fore.GREEN + "Tabla de resultados desde IPAPI")

                        print(
                            Style.RESET_ALL
                            + Fore.CYAN
                            + tabulate(response, tablefmt="fancy_grid")
                        )
                        print(" ")

                    elif op == 2:
                        os.system("cls" if os.name == "nt" else "clear")
                        ciclo = False
                        response = list(dani.ipapi_info().items())

                        print(" ")
                        bar2 = ChargingBar("Obteniendo informacion:", max=100)
                        for num in range(100):
                            time.sleep(random.uniform(0, 0.001))
                            bar2.next()
                        bar2.finish()
                        print(" ")

                        print(Fore.GREEN + "Tabla de resultados desde IPAPI")

                        print(
                            Style.RESET_ALL
                            + Fore.CYAN
                            + tabulate(response, tablefmt="fancy_grid")
                        )
                        print(" ")

                    else:
                        print(" ")
                        print(
                            Style.RESET_ALL
                            + Fore.RED
                            + "Lo sentimos no contamos con esa opcion :c"
                        )
                        print(" ")

                except ValueError:
                    print(" ")
                    print(Style.RESET_ALL + Fore.RED + "!Numero invalido!")
                    print(" ")

        elif menu == 0:
            print(" ")
            print(
                Style.RESET_ALL
                + Fore.CYAN
                + "################################################"
            )
            print(
                Style.RESET_ALL
                + Fore.CYAN
                + "GRACIAS POR SU PREFERENCIA, NOS VEMOS PRONTO :P"
            )
            print("################################################" +Style.RESET_ALL)
            break

        else:
            print(" ")
            print(
                Style.RESET_ALL
                + Fore.RED
                + "Ingresa un número que aparezca en la lista"
            )
            print(" ")

    except ValueError:
        print(" ")
        print(Style.RESET_ALL + Fore.RED + "Caracter invalido")
        print("")
