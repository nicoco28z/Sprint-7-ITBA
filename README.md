# Sprint-7-ITBA

## Descripción
Este repositorio contiene el código del proyecto homebanking. El objetivo principal de este sprint fue unir el front-end y el back-end del sistema.

## Modalidad de Trabajo
Para este proyecto, el equipo de desarrollo adoptó el framework DJANGO como estándar de trabajo. DJANGO facilita la creación rápida y efectiva de aplicaciones web, permitiendo una integración eficiente entre el front-end y el back-end.

## Problemas Abordados

### 1. Crear Modelo
Se creó el proyecto DJANGO homebanking, compuesto por diferentes aplicaciones como Clientes, Cuentas, Tarjetas, Movimientos, Prestamos, Autentificacion, entre otras. Utilizamos el modelo MVC, generando modelos para cada entidad que se requiere almacenar en la base de datos. Pudimos aprovechar la herramienta `inspectdb` para generar modelos automáticamente a partir de las entidades de la base de datos.

### 2. Crear Vistas
Desarrollamos las vistas necesarias para interactuar con el front-end. Cada vista maneja las peticiones de los usuarios y responde con la información adecuada. Estas vistas son esenciales para la futura construcción de una API con Django REST Framework en el siguiente sprint.

### 3. Autenticación
Implementamos el registro y autenticación de clientes utilizando el sistema provisto por DJANGO. Establecimos una relación 1 a 1 entre el usuario autenticado y la información del cliente almacenada. El homebanking ahora muestra el nombre del usuario autenticado y permite cerrar sesión en cualquier momento.

### 4. Formulario
Creamos una aplicación de préstamos con un formulario de solicitud de préstamos preaprobados. El formulario cuenta con protección contra Cross Site Request Forgery (CSRF). Los clientes pueden autenticarse para prellenar automáticamente sus datos. Además, el formulario valida el tipo de cliente y establece límites de monto de préstamo según la categoría (BLACK, GOLD, CLASSIC). Las solicitudes de préstamo se registran en la base de datos y afectan al préstamo y al saldo de la cuenta, proporcionando información sobre la aprobación o rechazo de la solicitud.

## Instrucciones de Uso
Para poner en marcha la aplicación, se deberán cumplir los siguientes pasos:

1. Abrir una consola de comandos.
2. Posicionarse en la carpeta 'Sprint-7-ITBA'.
3. Ejecutar el comando `py manage.py runserver`.

Es importante destacar que previamente debes contar con un entorno virtual con DJANGO instalado.

## Próximo Sprint
En el próximo sprint, nos enfocaremos en la construcción de una API utilizando Django REST Framework para mejorar la interacción entre el front-end y el back-end.

¡Gracias por revisar nuestro proyecto! Si tienes alguna pregunta o sugerencia, no dudes en ponerte en contacto con nosotros.
