from pydantic import BaseModel

class ContactoCreate(BaseModel):
    # Defino los campos obligatorios para crear un contacto.
    # Pydantic se encarga de revisar que sean texto (str) y que no vengan vacíos.
    email: str
    firstname: str
    lastname: str