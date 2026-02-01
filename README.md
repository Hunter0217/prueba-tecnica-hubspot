#  Microservicio de Integración CRM (HubSpot)

Este proyecto implementa una solución backend robusta y escalable para la **gestión centralizada de contactos**.

###  Problema que resuelve
En entornos empresariales distribuidos, la creación de prospectos (leads) suele ser inconsistente e insegura. Este microservicio actúa como una **puerta de enlace validada** entre los clientes externos y el CRM de HubSpot, asegurando que:
1.  No se inserten datos "basura" en el CRM (Validación estricta).
2.  Las credenciales sensibles del CRM no queden expuestas al frontend (Seguridad).
3.  Exista un punto único de entrada para auditar la creación de contactos.

---

##  Decisiones Técnicas y Arquitectura

Se ha optado por una **Arquitectura en Capas** (Controller-Service-Model) para garantizar el principio de responsabilidad única (SRP).

### Tecnologías Clave
* **Python 3.13 + FastAPI:** Elegido por su alto rendimiento (asincronía) y su capacidad de generar documentación automática (OpenAPI), reduciendo el tiempo de desarrollo.
* **Pydantic:** Utilizado para la **integridad de datos**. A diferencia de una validación manual con `if/else`, Pydantic asegura que los datos cumplan estrictamente con los contratos de interfaz antes de procesarlos.
* **Pydantic-Settings:** Para la gestión de configuración. Permite adherirse a los principios de **The Twelve-Factor App**, separando estrictamente la configuración (credenciales) del código fuente.
* **Requests:** Para la comunicación HTTP síncrona y fiable con la API de HubSpot.

---

##  Guía de Uso (API Reference)

### 1. Crear un Contacto (POST)
Permite registrar un nuevo prospecto. El sistema validará que el email tenga formato correcto y los campos no estén vacíos.

**Endpoint:** POST /crm/v3/objects/contacts

**Ejemplo de Petición (Request):**
```json
{
  "email": "nuevo_cliente@empresa.com",
  "firstname": "Ana",
  "lastname": "García"
}
```

### 2. Consultar Contactos (GET)
Obtiene los contactos más recientes almacenados en el CRM, filtrando la respuesta para entregar solo la información relevante para el negocio (email, nombre, fecha de creación).

**Endpoint:** `GET /crm/v3/objects/contacts`

**Respuesta Exitosa (200 OK):**
```json
{
  "results": [
    {
      "id": "123456",
      "properties": {
        "email": "cliente@ejemplo.com",
        "firstname": "Juan",
        "lastname": "Pérez",
        "createdate": "2026-01-31T10:00:00Z"
      }
    },
    {
      "id": "789012",
      "properties": {
        "email": "maria.gomez@test.com",
        "firstname": "Maria",
        "lastname": "Gomez",
        "createdate": "2026-02-01T14:30:00Z"
      }
    }
  ]
}