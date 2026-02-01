import uvicorn
from fastapi import FastAPI, HTTPException
from app.models.contact import ContactoCreate
from app.services.hubspot_service import crear_contacto_en_hubspot, obtener_contactos_de_hubspot

app = FastAPI()

# 1. Endpoint para CREAR (POST)
# Aquí recibimos los datos, Pydantic los revisa automáticamente y si todo está bien, pasamos.
@app.post("/crear-contacto")
def crear_contacto(contacto: ContactoCreate):
    try:
        # Le paso los datos limpios a mi servicio para que hable con HubSpot
        respuesta = crear_contacto_en_hubspot(contacto)

        # A veces HubSpot responde "200 OK" pero con un mensaje de error dentro.
        # Aquí revisamos eso para no engañar al usuario.
        if "status" in respuesta and respuesta["status"] == "error":
            raise HTTPException(status_code=400, detail=respuesta["message"])

        return {"mensaje": "Contacto creado con éxito", "hubspot_data": respuesta}

    except Exception as e:
        # Si ocurre un error inesperado (se cae internet, clave mal, etc), lanzo un error 500
        raise HTTPException(status_code=500, detail=str(e))

# 2. Endpoint para CONSULTAR (GET)
@app.get("/contactos")
def listar_contactos():
    try:
        # Llamo a la función que trae la lista
        respuesta = obtener_contactos_de_hubspot()

        # Misma validación de seguridad: si HubSpot se queja, yo me quejo.
        if "status" in respuesta and respuesta["status"] == "error":
            raise HTTPException(status_code=400, detail=respuesta["message"])

        return respuesta

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    # Arranco el servidor en el puerto 8000.
    # 'reload=True' me sirve para desarrollar, así no tengo que reiniciar a cada rato.
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)

