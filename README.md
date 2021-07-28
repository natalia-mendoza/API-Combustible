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

## Versión (Python 3.7)

#### 1.0.0

Funcionalidad: Base Calendarizable

## Contribuidor(es)

* #### 1. Andrés Henao Restrepo

  _rol:_ Contribuidor
  _usuario de Red:_  andres callejas
  _correo:_ ancallej@bancolombia.com.co

## Librerias:

'orquestador',
'sparky-bc',
'openpyxl',
'apscheduler',
'sklearn',
'pyodbc'
