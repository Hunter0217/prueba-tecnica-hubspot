import uvicorn
from fastapi import FastAPI, HTTPException
from app.models.contact import ContactoCreate
from app.services.hubspot_service import crear_contacto_en_hubspot, obtener_contactos_de_hubspot

app = FastAPI()

# 1. Endpoint para CREAR (POST)
# CORRECCIÓN: Usamos la ruta exacta sugerida en el documento
@app.post("/crm/v3/objects/contacts")
def crear_contacto(contacto: ContactoCreate):
    try:
        # Llamamos al servicio
        respuesta = crear_contacto_en_hubspot(contacto)

        # Validación de errores de HubSpot
        if "status" in respuesta and respuesta["status"] == "error":
            raise HTTPException(status_code=400, detail=respuesta["message"])

        return {"mensaje": "Contacto creado con éxito", "hubspot_data": respuesta}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 2. Endpoint para CONSULTAR (GET)
# CORRECCIÓN: Usamos la ruta exacta sugerida en el documento
@app.get("/crm/v3/objects/contacts")
def listar_contactos():
    try:
        respuesta = obtener_contactos_de_hubspot()

        if "status" in respuesta and respuesta["status"] == "error":
            raise HTTPException(status_code=400, detail=respuesta["message"])

        return respuesta

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)

