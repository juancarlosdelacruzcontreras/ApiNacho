#Cesar Santuaio 21/07/2021
#Módulo para el funcionamiento de la API de http://api.ipstack.com
import httpx
import ipaddress
import os

ENDPOINT = "http://api.ipstack.com/"
APIKEY = "85bf7856115802d67fb05963826e962d"

def ipstack_info() -> httpx.Response:
    """Solicitud a la API api.ipstack.com

    Returns:
        httpx.Response: Respuesta de la API
    """
    os.system("cls" if os.name == "nt" else "clear") # Limpia pantalla
    while True:
        try:
            ip = input("Ingresa la dirección IP: ")
            ipaddress.ip_address(ip) # !https://stackoverflow.com/a/10782565
            os.system("cls" if os.name == "nt" else "clear")
            break
        except ValueError:
            print(f"La ip {ip} no parece ser una IP válida.\nPor favor vuelve a intentarlo.")

    uri = ENDPOINT + ip + "?access_key=" + APIKEY # Creando la URI con la IP ingresada
    with httpx.Client() as client:
        r = client.get(uri) # Mandando solicitud a la api
    return r.json() # Regresando la respuesta en formato JSON

# *https://youtu.be/AcNKU77vyjg?t=209 Min 3:29
