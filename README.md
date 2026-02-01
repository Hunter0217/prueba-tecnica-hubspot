# Integración con HubSpot API (Prueba Técnica)

Este proyecto implementa un microservicio con FastAPI que permite crear contactos en HubSpot CRM de forma segura y validada.

## Tecnologías

* **Python 3.13**
* **FastAPI:** Para la creación del API REST.
* **Pydantic:** Para validación de datos y manejo de configuración (.env).
* **Requests:** Para la comunicación con la API externa de HubSpot.

## Instalación y Configuración

1.  **Clonar o descargar el proyecto.**
2.  **Crear entorno virtual** (si no lo hace el IDE automáticamente):
    ```bash
    python -m venv .venv
    ```
3.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Configurar Variables de Entorno:**
    * Crear un archivo `.env` en la raíz del proyecto.
    * Agregar el token de HubSpot:
        ```env
        HUBSPOT_ACCESS_TOKEN=tu_token_aqui
        ```

##  Ejecución

Para iniciar el servidor de desarrollo:

```bash
uvicorn app.main:app --reload