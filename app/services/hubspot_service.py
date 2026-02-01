import requests
from app.config.settings import settings
# Importo el modelo para tener autocompletado y saber qué datos llegan
from app.models.contact import ContactoCreate

def crear_contacto_en_hubspot(datos: ContactoCreate):
    # Endpoint oficial de HubSpot para crear contactos
    url = "https://api.hubapi.com/crm/v3/objects/contacts"

    # Configuro la autenticación y el tipo de contenido
    headers = {
        "Authorization": f"Bearer {settings.HUBSPOT_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    # Organizo los datos en la estructura que exige HubSpot ("properties")
    payload = {
        "properties": {
            "email": datos.email,
            "firstname": datos.firstname,
            "lastname": datos.lastname
        }
    }

    # Hago la petición POST para enviar la información
    response = requests.post(url, headers=headers, json=payload)

    return response.json()

def obtener_contactos_de_hubspot():
    url = "https://api.hubapi.com/crm/v3/objects/contacts"

    headers = {
        "Authorization": f"Bearer {settings.HUBSPOT_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    # Defino qué campos quiero recibir. Si no pongo esto, HubSpot trae muy poco.
    params = {
        "properties": "email,firstname,lastname,createdate",
        "limit": 10
    }

    # Uso GET porque solo estoy consultando información
    # Nota: Aquí paso 'params' en lugar de 'json' porque van en la URL
    response = requests.get(url, headers=headers, params=params)

    return response.json()