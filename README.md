
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


* Ahora debe abrir dos terminales de **Window**, ir la carpeta base del proyecto y ejeuctar los siguientes comandos en una terminal y el otro ando en la otra terminal

![Captura](https://user-images.githubusercontent.com/78820446/121410661-70023600-c928-11eb-807e-8ebfcb3cd2b2.JPG)


1. Primer comando rasa **rasa run actions**:
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

# Ejecutando pruebas E2E sobre Ghost 3.3.0 ⚙️

Para ejecutar unicamente debe  hacer lo siguiente:

1. **Para ejecutar las pruebas de la versión Ghost 3.3.0** debe ejecutar el comando **git checkout Ghost3.3.0**
2. Asegurese de haber inicializado ghost en la versión 3.3.0
3. Luego deberá modificar las variables **USER** y **PASSWORD** en el archivo **kraken_mobile_properties.json**, que está ubicado dentro de la carpeta **proyecto**, con sus credenciales registradas en Ghost 3.3.0. **Por ejemplo:

    **"USER":"arodriguezt9509@gmail.com",**
 
    **"PASSWORD":"********"
      
4. Asegurese de tener la vista del sitio como **pública**. Para esto debe ir a "General Settings" en Ghost y en la sección "Advanced Settings" debe tener deshabilitada la opción de "Make this site private", como se observa a continuación.

5. Por último, ejecute el siguiente comando: **bundle exec kraken-mobile run --properties=./kraken_mobile_properties.json**, en este caso si realizo las configuraciones de una manera correcta deberán empezar a ejecutarse los tests, en caso contrario deberaá revisar alguno de los pasos de instalación. 

# Ejecutando pruebas E2E sobre Ghost 3.42.5 ⚙️

Para ejecutar unicamente debe  hacer lo siguiente:

1. **Para ejecutar las pruebas de la versión Ghost 3.42.5** debe ejecutar el comando **git checkout Ghost3.42.5**
2. Asegurese de haber inicializado Ghost en la versión 3.42.5
3. Luego deberá modificar las variables **USER** y **PASSWORD** en el archivo **kraken_mobile_properties.json**, ue está ubicado dentro de la carpeta **proyecto**, con sus credenciales registradas en Ghost 3.42.5. **Por ejemplo:

    **"USER":"arodriguezt9509@gmail.com",**
 
    **"PASSWORD":"********"
    
4.  Asegurese de tener la vista del sitio como **pública**. Para esto debe ir a "General Settings" en Ghost y en la sección "Advanced Settings" debe tener deshabilitada la opción de "Make this site private", como se observa a continuación.

![image](https://user-images.githubusercontent.com/78829003/117516478-d75e4c00-af5e-11eb-8002-3ff61f2e25d6.png)

5. Por último, ejecute el siguiente comando: **bundle exec kraken-mobile run --properties=./kraken_mobile_properties.json**, en este caso si realizo las configuraciones de una manera correcta deberán empezar a ejecutarse los tests, en caso contrario deberaá revisar alguno de los pasos de instalación. 


### Analice las pruebas end-to-end 🔩

En este caso para el analizis de las pruebas ejecutadas unicamente debe evidenciar los resultados de la consola y ver los resultados en la carpeta **JWDA-Kraken-Semana5\proyecto\reports**

# Ejecutando VRT con Resemble.js ⚙️

Para ejecutar debe  hacer lo siguiente:

1. **Para ejecutar VRT en Resemble.js** debe ejecutar el comando **git checkout Resemble/Semana6**
2. Luego de moverse a la rama Resemble/Semana6 debe ir a la carpeta **resemble** ejecutando el siguiente comando **cd resemble**
3. Allí deberá ejecutar el comando **npm install**
4. En el archivo **index.js** que se encuentra dentro de la carpeta **resemble** deberá modificar el path que contiene a la carpeta **resemble**, como se indica en la siguiente imagen:

![image](https://user-images.githubusercontent.com/78829003/118384661-7f15f280-b5cd-11eb-8467-f3b1a93bc2b5.png)
5. Para ejecutar el vrt para cada uno de los escenarios deberá modificar la variable **scenario** y la variable **steps**, teniendo en cuenta lo siguiente:

![image](https://user-images.githubusercontent.com/78829003/118384817-d6689280-b5ce-11eb-90d3-2f21376cf51e.png)

|Scenario|Steps|
|--------|-----|
|Login_invalid_user_invalid_pass|6|
|Login_invalid_user_valid_pass|6|
|Manage_settings_change_timezone|10|
|Manage_settings_make_private|9|
|Pages_filter_by_item_1st|11|
|Pages_filter_by_item_1st_to_4th|17|
|Post_creation_new_post_button|13|
|Post_creation_scheduled|19|
|Tag_manage_add_metadata|16|
|Tag_manage_delete_tag|13|


6. Luego de modificar las variables anteriores, deberá ejecutar el comando **node index.js** lo cual le creará una carpeta dentro de la carpeta **results** con el nombre del escenario ejecutado. Dentro de esta carpeta encontrará las imágenes del resultado de las comparaciones realizadas paso a paso y el reporte de cada una de estas comparaciones, igualmente por cada paso.

![image](https://user-images.githubusercontent.com/78829003/118384703-ecc21e80-b5cd-11eb-8b9c-41c7bc78ceef.png)

### Analice el vrt con Resemble🔩

Para cada uno de los escenarios ejecutados, encontrará dentro de la carpeta **results** una carpeta con el nombre del escenario. Dentro de esta carpeta podrá visualizar las imágenes del resultado de la comparación de cada uno de los pasos ejecutados en el escenario para Ghost 3.3.0 y Ghost 3.42.5. Igualmente podrá visualizar un reporte que le mostrará la imagen del paso ejecutado en Ghost 3.3.0, la imagen del paso ejecutado en Ghost 3.42.5 y las diferencias entre estas dos imágenes:

![image](https://user-images.githubusercontent.com/78829003/118384789-973a4180-b5ce-11eb-83c6-55d8c6132bd2.png)

# Ejecutando VRT con Backstop.js ⚙️

Para ejecutar debe  hacer lo siguiente:

1. **Para ejecutar VRT en Resemble.js** debe descargar la CLI. Para esto abra una terminal y ejecute el comando **npm install -g backstopjs**
2. Luego debe moverse a la rama  Backstop/Semana6  ejecutando el comando **git checkout Backstop/Semana6** 
3. Luego de moverse a la rama  Backstop/Semana6 debe ir a la carpeta **backstop** ejecutando el siguiente comando **cd backstop**
4. Allí deberá ejecutar el comando **backstop test**
5. Esto le abrirá una ventana en el browser que le mostrará el resultado para cada uno de los pasos del escenario Login with invalid user and valid password.

### Analice el vrt con Backstop 🔩

Luego de ejecutar el comando backstop test se le abrirá automaticamente una nueva ventana en el browser la cual mostrará el reporte con los resultados obtenidos. Para cada uno de los pasos del escenario se mostrará la imagen de referencia, la imagen de test y la imagen con las diferencias. Estos resultados se mostrán para dos tipos de pantallas.

![image](https://user-images.githubusercontent.com/78829003/118386658-ab863a80-b5de-11eb-8deb-614b6a3645d8.png)

# Ejecutando pruebas E2E con pool de datos pseudo-aleatorio dinámico sobre Ghost 3.42.5 ⚙️

Para ejecutar las pruebas e2e con pool de datos pseudo-aleatorio dinámico estamos usando la herramienta **Mockaroo** y un script en **Python3** llamado **readmockaroo.py**. El script se encarga de generar los datos pseudo-aleatorios antes que se realicen las pruebas. Como requisito se debe tener installado **[Python3](https://www.python.org/downloads/)** y la librería de python **[requests](https://pypi.org/project/requests/)**. 

1. **Para ejecutar las pruebas con pool de datos pseudo-aleatorio dinámico sobre la versión Ghost 3.42.5** debe ejecutar el comando **git checkout feature/jb_pool_mockaroo**
2. Asegurese de haber inicializado Ghost en la versión 3.42.5
3. Moverse a la carpeta proyecto con el siguiente comando **cd proyecto**
4. Luego deberá modificar las variables **USER** y **PASSWORD** en el archivo **credentials.json**, que está ubicado en la carpeta **proyecto**, con sus credenciales registradas en Ghost 3.42.5. **Por ejemplo:

    **"USER":"prueba@gmail.com",**
 
    **"PASSWORD":"********"
      
5. Genere los datos pseudo-aleatorios con el siguiente comando **python3 readmockaroo.py**
6. Luego de ejecutado el script podrá verificar que el archivo **kraken_properties_mockaroo.json** se ha modificado con sus credenciales y otras variables que tienen valores aleatorios generados en **Mockaroo** que se usarán en las pruebas.  
7. Por último, ejecute el siguiente comando: **bundle exec kraken-mobile run --properties=./kraken_properties_mockaroo.json**, en este caso si realizo las configuraciones de una manera correcta deberán empezar a ejecutarse los tests, en caso contrario deberá revisar alguno de los pasos de instalación. 
8. Si desea, puede actualizar el pool de datos corriendo nuevamente el script de python para realizar las pruebas con nuevos datos

En caso de que alguno de los escenarios de prueba falle, puede deberse a que en la generación de datos con **Mockaroo** a algunas de las variables hemos configurado para que en un 20% de las veces genere datos NULL.

## Pasos para ejecutar el Generador.jar para las pruebas E2E sobre Ghost 3.42.5: Este tiene cubrimientos para generar  los diferentes tipos de datos **Prioriatio, Complemento del pseudo y aleatorio**

* Clonar el repositorio **https://github.com/Alejito29/JWDA-Kraken-Semana5**

* Ubicarse en la rama **feature/ag_kraken_data**

* Abrir el ejecutable **Generador.jar** que se encuentra en la raiz del proyecto, en caso de ser sistema operativo linux debe ejecutarlo con la terminal, si es mac o windows unicamente debe darle doble click, como requisito es necesario que tenga instalado JAVA  1.7.

![Evidenica jar2](https://user-images.githubusercontent.com/78820446/119274217-70829900-bbd4-11eb-989e-1825cb0150da.png)


* Por ultimo debe escoger el nombre del test, cuantas veces se va repetir la creacion y que tipo de dato desea. Con el jar podra crear diferentes tipos de datos, en este caso usted define cuanto dataset desea generar, aunque si genera el maximo cubriria los casos solicitados solo que se demoraria la ejecucion.

 ![Evidenica jar](https://user-images.githubusercontent.com/78820446/119274137-1bdf1e00-bbd4-11eb-9f1e-ab7cb971bb13.png)

Observacion en la wiki se encuentra el detalle tecnico como ejecutar cada prueba con los diferentes tipos de datos 

* https://github.com/Alejito29/JWDA-Kraken-Semana5/wiki/Pool-de-datos-Apriori
* https://github.com/Alejito29/JWDA-Kraken-Semana5/wiki/Pool-de-datos-pseudo-aleatorio-din%C3%A1mico
* https://github.com/Alejito29/JWDA-Kraken-Semana5/wiki/Aleatorio

Adicional en caso que desen tener acceso al fuente del codigo java lo encontraran aca **https://github.com/Alejito29/JWDA-Java-Semana7**

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

* **Wilson Alejandro Gonzalez Gaitan** - *Trabajo Inicial* - [Alejito29](https://github.com/Alejito29)
* **Dario Fernando Herrera Gonzalez** - *Trabajo Inicial* - [dherrera54](https://github.com/dherrera54)
* **Angelica Maria Rodriguez Torres** - *Trabajo Inicial* - [angelicamariarodriguez](https://github.com/angelicamariarodriguez9)
* **Jorge Ivan Barrera Rea** - *Trabajo Inicial* - [ivanbrij](https://github.com/ivanbrij)




## Licencia 📄

Este proyecto está bajo la Licencia (Copyleft) - mira el archivo [LICENSE.md](LICENSE.md) para detalles

