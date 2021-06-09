
# RASA 

Rasa is the leading conversational AI platform, for personalized conversations at scale.


# RASA 

Este proyecto contiene el codigo fuente creado en RASA que permite emular un chat bot.

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

Mira **Deployment** para conocer como desplegar el proyecto.


### Pre-requisitos 📋

Para poder ejecutar de manera correcta el proyecto debe tener configurado las siguientes herramientas en su maquina

```
Node,              Version  12.17.0
Chrome,            Version  90.0.4430.93
Git,               Version  2.21.0
Java               Version  1.8.0_91
Chromium           Version  92.0.4499.0
Python             Version  3.8.10
Rasa               Version  3.8.10
```

### Instalación 🔧

En este caso para ejecutar el proyecto debe haber instalado las herramientas indicadas anteriormente en el paso de **Pre-requisitos**, una vez instaladas debe ejecutar lo siguiente 

Pasos

```
Revisar que se encuentre configurado node de manera correcta, se realiza de la siguiente manera
```

* Abrir la terminal de su equipo, esta guia estara para un sistema operativo Windows, pero si configuro de manera exitosa las herramientas nombradas en  **Pre-requisitos** no deberia haber diferencia.

![Terminal](https://user-images.githubusercontent.com/78820446/117479939-8cc0dd80-af26-11eb-85a5-b3559aa18ac5.PNG)


* Ejecutar el comando node -v en la terminal, si aparece la version  esto indicaria que se encuentre instalado de manera correcta, en caso contrario debera revisar la instalacion de node en su maquina 

![Node ](https://user-images.githubusercontent.com/78820446/117480756-9eef4b80-af27-11eb-98bd-cb7756ef43ac.PNG)



El siguiente paso 

```
Revisar que tenga instalado git en su maquina, se realiza de la siguiente manera
```

* Abrir la terminal de su equipo, puede ser la misma que abrio en el paso anterior para verificar  la instalacion de node

![Terminal](https://user-images.githubusercontent.com/78820446/117479939-8cc0dd80-af26-11eb-85a5-b3559aa18ac5.PNG)

* Ahora ejecutar el siguiente comando **git --version**, en caso que no aparesca la version debera revisar la instalacion de git

![git](https://user-images.githubusercontent.com/78820446/117470240-351d7480-af1c-11eb-9032-03f81b674975.PNG)


El siguiente paso 

```
Revisar que tenga instalado python en su maquina, se realiza de la siguiente manera. En caso que no aparesca debe verificar la instalacion y configuracion de python
```

* Abrir la terminal de su equipo, puede ser la misma que abrio en el paso anterior y ejecutar el siguiente comando **python --version**

![Captura](https://user-images.githubusercontent.com/78820446/121415438-5adbd600-c92d-11eb-8967-8f3ab2bdd7af.JPG)


El siguiente paso

```
Revisar que tenga instalado java  y configurado 
```

* Sobre la terminal ejecutada debe ejecutar el siguiente comando **java  -version** en caso que no aparesca la version deberia revisar la instalacion 

![Java](https://user-images.githubusercontent.com/78820446/117546069-2ef7c880-afee-11eb-9eda-64cd2bdd8a10.PNG)

* Si se reconoce el comando **java -version** debera configurar las siguientes variables de entorno en el computador 

  - JAVA_HOME Ingresar la ruta donde se encuentra instalado su JDK 

![JAVA ENTORNO](https://user-images.githubusercontent.com/78820446/117546738-80558700-aff1-11eb-85c4-91102e2994dd.PNG)

  - Adicional agregar las siguientes variables de entorno en la opcion de **path**:  **%JAVA_HOME%\bin** 

![JAVA ENTORNO](https://user-images.githubusercontent.com/78820446/117546768-b72b9d00-aff1-11eb-9bc9-324525a90433.PNG)



El siguiente paso 


```
Clonar el repositorio a traves de git siguiendo los siguientes pasos 
```

* Crear una carpeta vacia en cualquier ubicacion de su equipo, es importante que no contenga espacios en blanco 
 
* Abrir la terminal y ubicarse en la ruta donde se encuentra creada la carpeta a traves de la terminal 


* Clonar el repositorio a traves del siguiente commando  **git clone https://github.com/Alejito29/Rasa-x![Captura]
**

![git](https://user-images.githubusercontent.com/78820446/121409075-afc81e00-c926-11eb-8547-aff4764904e5.JPG)




El siguiente paso 


```
Dirigirse a  la carpeta clonada con la terminal del paso anterior 
```

* Sobre la carpeta creada en el paso anterior y el proyecto clonado, debe ejecutarse el siguiente comando **cd Rasa-x**

![Captura](https://user-images.githubusercontent.com/78820446/121409461-2c5afc80-c927-11eb-9734-de95ec51b429.JPG)


* Ahora debe abrir dos terminales de **Window**, ir la carpeta base del proyecto y ejecutar los siguientes comandos en una terminal y el otro comando  en la otra terminal

![Captura](https://user-images.githubusercontent.com/78820446/121410661-70023600-c928-11eb-807e-8ebfcb3cd2b2.JPG)


1. Primer comando rasa **rasa run actions**, pero antes de ejecutar el comando debe configurar el apuntamiento de los folder donde se encuentra la plantilla, ejemplo ***Rasa-x\Formularios\Plantilla**
    
    - Este comando inicia a escuchar las acciones que se van tener en rasa

![Captura](https://user-images.githubusercontent.com/78820446/121411548-5f05f480-c929-11eb-8ece-ddef68e988c9.JPG)


```
Debe salir el siguiente mensaje en la consola 

ide at https://www.tensorflow.org/install/gpu for how to download and setup the required libraries for your platform.
Skipping registering GPU devices...
2021-06-09 13:44:59 INFO     rasa_sdk.endpoint  - Starting action endpoint server...
2021-06-09 13:44:59 INFO     rasa_sdk.executor  - Registered function for 'action_save_data_in_storage'.
2021-06-09 13:44:59 INFO     rasa_sdk.executor  - Registered function for 'action_ask_last_name'.
2021-06-09 13:44:59 INFO     rasa_sdk.executor  - Registered function for 'action_restart'.
2021-06-09 13:44:59 INFO     rasa_sdk.executor  - Registered function for 'action_reset_all_slots'.
2021-06-09 13:44:59 INFO     rasa_sdk.executor  - Registered function for 'action_ask_ticket_reservation'.
2021-06-09 13:44:59 INFO     rasa_sdk.executor  - Registered function for 'action_ask_expense'.
2021-06-09 13:44:59 INFO     rasa_sdk.executor  - Registered function for 'action_ask_the_report_room'.
2021-06-09 13:44:59 INFO     rasa_sdk.executor  - Registered function for 'action_ask_the_report_user'.
2021-06-09 13:44:59 INFO     rasa_sdk.executor  - Registered function for 'action_ask_the_report_reservation'.
2021-06-09 13:44:59 INFO     rasa_sdk.executor  - Registered function for 'action_ask_the_report_expense'.
2021-06-09 13:44:59 INFO     rasa_sdk.executor  - Registered function for 'action_ask_the_report_all'.
2021-06-09 13:44:59 INFO     rasa_sdk.endpoint  - Action endpoint is up and running on http://localhost:5055

```
2. Segundo comando **rasa shell**:
    - Este comando inicia rasa para empezar a interactuar con el chat bot en base a las intenciones

![Captura](https://user-images.githubusercontent.com/78820446/121412207-0f73f880-c92a-11eb-8fac-b08f42b06a99.JPG)

```
Debe salir el siguiente mensaje en la consola 

ide at https://www.tensorflow.org/install/gpu for how to download and setup the required libraries for your platform.
Skipping registering GPU devices...
2021-06-09 13:44:59 INFO     rasa_sdk.endpoint  - Starting action endpoint server...
2021-06-09 13:44:59 INFO     rasa_sdk.executor  - Registered function for 'action_save_data_in_storage'.
2021-06-09 13:44:59 INFO     rasa_sdk.executor  - Registered function for 'action_ask_last_name'.
2021-06-09 13:44:59 INFO     rasa_sdk.executor  - Registered function for 'action_restart'.
2021-06-09 13:44:59 INFO     rasa_sdk.executor  - Registered function for 'action_reset_all_slots'.
2021-06-09 13:44:59 INFO     rasa_sdk.executor  - Registered function for 'action_ask_ticket_reservation'.
2021-06-09 13:44:59 INFO     rasa_sdk.executor  - Registered function for 'action_ask_expense'.
2021-06-09 13:44:59 INFO     rasa_sdk.executor  - Registered function for 'action_ask_the_report_room'.
2021-06-09 13:44:59 INFO     rasa_sdk.executor  - Registered function for 'action_ask_the_report_user'.
2021-06-09 13:44:59 INFO     rasa_sdk.executor  - Registered function for 'action_ask_the_report_reservation'.
2021-06-09 13:44:59 INFO     rasa_sdk.executor  - Registered function for 'action_ask_the_report_expense'.
2021-06-09 13:44:59 INFO     rasa_sdk.executor  - Registered function for 'action_ask_the_report_all'.
2021-06-09 13:44:59 INFO     rasa_sdk.endpoint  - Action endpoint is up and running on http://localhost:5055

```
3. Debe abrir el jar ubicado dentro de la carpeta del proyecto, este se ubica en **Rasa-x\Formularios**, antes de abrir el programa por favor cambiar los siguientes parametros dentro del archivo **Config.properties**

    - Actualizar la key config.enpoint.database=C:/Users/wilso/Desktop/rasa/profile.db por la nueva ruta, la base de datos se ubica en el mismo proyecto clonado llamado. Es importante que la ruta la deja con **/** 
    
    ![Captura](https://user-images.githubusercontent.com/78820446/121419940-2585b700-c932-11eb-82bf-ebf9be3f6460.JPG)

    ![Captura](https://user-images.githubusercontent.com/78820446/121420206-6aa9e900-c932-11eb-86b8-c9069739ab2d.JPG)

    - Con ese **JAR** contiene para interactuar con la reservacion, actualizar las reservas, y añadir gasto. Unicamente debe darle doble click al programa si tiene configurado correactamente java

![Captura](https://user-images.githubusercontent.com/78820446/121420563-d724e800-c932-11eb-961b-8db14b41a75c.JPG)


## Funcionalidades y estrategias 🚗

Este proyecto está probando las siguientes funcionalidades:

1. Gestionar las reservas de habitaciones:
    - Crear una reservacion
2. Gestionar las habitaciones libres/ocupadas:
    - Reservar habitacion
    - Dejar libre el cuarto
3. Gestionar gastos extras:
    - Añadir gasto asociado a un ticket
 4. Facturar a los clientes:
    - Generar la facturacion del cliente en base al ticket
 5. Permitir listados y estadísticas:
    - Crear reporte de los cuartos
    - Crear reporte de los usuarios
    - Crear reporte de las reservaciones
    - Crear reporte de los gastos
    - Crear reporte aglomerado.

# Interactuando con rasa ⚙️

Para interactuar con rasa unicamente debe escribir algun texto, en este caso las intenciones programadas en rasa fueron las siguientes 


```
- intent: request_names
  examples: |
    - i want to deliver the room
- intent: request_statistics_rooms
  examples: |
    - please can you generate the reports  about rooms
- intent: request_statistics_user
  examples: |
    - could i look the report about user
- intent: request_statistics_reservation
  examples: |
    - please, I want to watch the reporrt about reservation
- intent: request_statistics_expense
  examples: |
    - i want to look the report about expense
- intent: request_statistics_all
  examples: |
    - please raza generates all reports

```

En caso que dese revisar las intenciones las podra encontrar en el siguiente enlace **https://github.com/Alejito29/Rasa-x/blob/master/data/nlu/nlu.yml**

Ahora unicamente debe escribir algunos de los textos indicados en las intenciones, comenzara a solicitar o procesar lo solicitado rasa.

![Captura](https://user-images.githubusercontent.com/78820446/121418373-814f4080-c930-11eb-91fd-3adadc8fcc62.JPG)


## Video de explicacion para ejecutar el Generador.jar 

En este enlace podrán encontrar un pequeño video donde explicamos la forma de  generar los datos antes de ejecutar los test de las diferentes formas

https://uniandes-my.sharepoint.com/:v:/g/personal/w_gonzalezg_uniandes_edu_co/ETYtwFw3lEFLjWN-SzKbImQBu4IktCsbP3a2f1IC2nfqHw?e=L7I2kB


### Analice las pruebas end-to-end con  los diferentes tipos de datos 🔩

En este caso para el analizis de las pruebas ejecutadas unicamente debe evidenciar los logs de la consola y ver los resultados en la carpeta **JWDA-Kraken-Semana5\proyecto\reports**

**NOTA: La descripción de la estrategia usada para la generación de datos y la definición de los oráculos, la puede encontrar como una página en la wiki de este repositorio.**


## Construido con 🛠️

_Menciona las herramientas que utilizaste para crear tu proyecto_

* [Node 12.17.0](https://nodejs.org/es/download/releases/) - Node
* [Cypress](https://www.cypress.io/) - Cypress
* [Android studio](https://developer.android.com/studio) - Android
* [Chromium](https://www.chromium.org/getting-involved/download-chromium) - Chromium
* [JAVA](https://www.java.com/es/download/ie_manual.jsp) - Java
* [Kraken](https://github.com/TheSoftwareDesignLab/KrakenMobile/archive/refs/tags/1.0.9.zip.) - Kraken
* [Chrome](https://www.google.com/intl/es/chrome/?brand=UUXU&gclid=CjwKCAjw7diEBhB-EiwAskVi10CI0gLPlO0E3zn_0-3gOnt60O2j_i2Jr_gHLJIEkfyP0JssFBki4hoC4sYQAvD_BwE&gclsrc=aw.ds) - Chrome
* [Javascript](https://developer.mozilla.org/es/docs/Web/JavaScript) - Javascript
* [Git](https://git-scm.com/downloads) - Git
* [Ghost](https://github.com/TryGhost/Ghost/tree/3.3.0) - Ghost
* [Chromedriver](https://chromedriver.chromium.org/downloads) - chromedriver
* [Ruby](https://rubyinstaller.org/) - Ruby

## Autores ✒️

_Autor_


## Licencia 📄

Este proyecto está bajo la Licencia (Copyleft) - mira el archivo [LICENSE.md](LICENSE.md) para detalles

