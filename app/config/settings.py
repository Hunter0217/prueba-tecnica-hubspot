import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Defino las variables obligatorias. Si no encuentra el token,
    # Pydantic detendrá la ejecución (validación automática).
    HUBSPOT_ACCESS_TOKEN: str

    model_config = SettingsConfigDict(
        # Construyo la ruta absoluta al archivo .env
        # Uso 'dirname' y 'abspath' para subir dos niveles desde esta carpeta
        # (de config/ -> app/ -> raíz del proyecto)
        env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../.env"),
        env_file_encoding="utf-8"
    )

# Creo una instancia única para importar la configuración desde otros archivos
settings = Settings()