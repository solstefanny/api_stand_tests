# API Stand Tests

## Descripción
Este proyecto contiene pruebas automatizadas para la API de Urban Grocers, específicamente para el endpoint de creación de usuarios.

## Funcionalidades
- Pruebas de validación para el campo `firstName`
- Verificación de códigos de respuesta HTTP
- Validación de creación exitosa de usuarios en la base de datos

## Archivos del proyecto
- `create_user_test.py` - Contiene las 10 pruebas automatizadas
- `sender_stand_request.py` - Funciones para enviar solicitudes HTTP
- `data.py` - Datos de prueba y configuración
- `configuration.py` - URLs y configuración del servidor

## Cómo ejecutar las pruebas
1. Instalar pytest: `pip install pytest`
2. Ejecutar todas las pruebas: `pytest create_user_test.py`
3. Ejecutar con detalles: `pytest -v create_user_test.py`

## Casos de prueba incluidos
- Validación de longitud mínima y máxima del firstName
- Pruebas con caracteres especiales, números y espacios
- Verificación de campos obligatorios