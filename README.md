## Introducción

El objetivo de este proyecto es tener una base de desarrollo analitico para su posterior puesta en produccion.

#### Instalación :

* 1. Crear ambiente virtual dentro de la carpeta del proyecto

  > pip install virtualenv (si no lo tiene instalado)
  > virtualenv venv
  >
* 2. Luego debe activar el entorno virtual

  > .\ venv\Scripts\activate
  >
* 3. Instalar librerias

  > pip install -r requirements.txt
  >

* 4. ejecutar los dos siguientes comandos en la terminal

  > $env:FLASK_APP = "app.py" 
  >
  > $env:FLASK_ENV = "development"
  >


#### Ejecución:

* 1. Despues de tener las librerias instaladas

  > flask run
  >


