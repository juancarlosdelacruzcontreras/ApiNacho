#Ricardo 23/07/2021
#Módulo para el funcionamiento de la API de http://api.ipapi.com/
import requests
import os
import ipaddress

ENDPOINT = "http://api.ipapi.com/"
APIKEY = "746b05ad74bb7f91d7ff8f52262776ab"

c = requests.get(ENDPOINT)

if c.status_code == 200:
    def ipapi_info():
        """Solicitud a la API api.ipapi.com/
        Returns:
            request.get: Respuesta de la API
        """
        os.system("cls" if os.name == "nt" else "clear") # Limpia pantalla
        
        while True:
            try:
                ip = input("Ingresa la direccion IP: ")
                ipaddress.ip_address(ip)
                os.system("cls" if os.name == "nt" else "clear")
                break
            except ValueError:
                print(f"La {ip} no parece ser una IP valida\n Vuelva a intentarlo.")
                
        uri = ENDPOINT + ip + "?access_key=" + APIKEY
        response = requests.get(uri)
        response_json = response.json()
        
        return response_json
            



