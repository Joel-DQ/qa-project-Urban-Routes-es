# Sprint 9: Automatización de pruebas de la aplicación web Urban Routes

## Descripción del proyecto

Este proyecto consiste en la **automatización de pruebas funcionales de la aplicación web Urban Routes**, utilizando Selenium WebDriver y Pytest.

El objetivo principal es comprobar mediante pruebas automatizadas el proceso de solicitud de un taxi y verificar que las diferentes funcionalidades de la aplicación respondan correctamente a las acciones realizadas por el usuario.

Las pruebas se encuentran implementadas en el archivo `main.py`, donde se utiliza el patrón **Page Object Model (POM)** para separar los localizadores y métodos de interacción con la aplicación de los casos de prueba.

## Funcionalidades automatizadas

Las pruebas automatizadas cubren el flujo de solicitud de un taxi, incluyendo:

1. Configuración de la dirección de origen.
2. Configuración de la dirección de destino.
3. Selección de la tarifa **Comfort**.
4. Introducción y confirmación del número de teléfono.
5. Agregado de una tarjeta bancaria como método de pago.
6. Introducción de un mensaje para el conductor.
7. Selección de la opción de manta y pañuelos.
8. Agregado de dos helados al pedido.
9. Solicitud del taxi.
10. Verificación de la aparición del modal de búsqueda de automóvil.
11. Espera de la información del conductor.

## Tecnologías utilizadas

El proyecto utiliza las siguientes tecnologías y herramientas:

* **Python**: lenguaje de programación utilizado para desarrollar las pruebas automatizadas.
* **Selenium WebDriver**: herramienta utilizada para automatizar la interacción con el navegador y los elementos de la aplicación web.
* **Pytest**: framework utilizado para organizar y ejecutar las pruebas automatizadas.
* **WebDriverWait**: mecanismo de Selenium utilizado para realizar esperas explícitas y sincronizar las pruebas con el estado de la aplicación.
* **Expected Conditions (`expected_conditions`)**: condiciones utilizadas junto con `WebDriverWait` para esperar a que los elementos estén visibles, disponibles o contengan determinados textos.
* **Page Object Model (POM)**: patrón de diseño utilizado para organizar los localizadores y métodos de interacción con la página.

## Estructura del proyecto

La estructura principal del proyecto es:

```text
.
├── main.py
├── data.py
└── README.md
```

### `main.py`

Contiene:

* La clase `UrbanRoutesPage`, que incluye los localizadores y métodos necesarios para interactuar con Urban Routes.
* La clase `TestUrbanRoutes`, que contiene las pruebas automatizadas del flujo de solicitud de un taxi.

### `data.py`

Contiene los datos utilizados durante las pruebas, como:

* URL de Urban Routes.
* Dirección de origen.
* Dirección de destino.
* Número de teléfono.
* Datos necesarios para las pruebas de pago.
* Otros datos utilizados por los casos de prueba.

### `README.md`

Contiene la descripción del proyecto, las tecnologías utilizadas y las instrucciones necesarias para ejecutar las pruebas.

## Técnicas de automatización utilizadas

### Localizadores

Para localizar los elementos de la interfaz se utilizan diferentes estrategias de Selenium, entre ellas:

* `By.ID`
* `By.CSS_SELECTOR`
* `By.CLASS_NAME`
* `By.XPATH`

Esto permite identificar diferentes elementos de la aplicación, como campos de texto, botones, opciones de tarifa, métodos de pago y controles del pedido.

### Interacción con elementos

Las pruebas realizan diferentes tipos de interacción con la aplicación:

* Introducción de texto mediante `send_keys()`.
* Clic en botones y elementos interactivos.
* Selección de opciones.
* Uso de teclas como `TAB` para cambiar el foco de un campo.
* Lectura de valores y textos de los elementos para realizar verificaciones.

### Esperas explícitas

Se utiliza `WebDriverWait` junto con condiciones esperadas de Selenium para evitar que las pruebas intenten interactuar con elementos antes de que estén disponibles.

Entre las condiciones utilizadas se encuentran:

* `visibility_of_element_located`
* `element_to_be_clickable`
* `text_to_be_present_in_element`

Estas esperas ayudan a que las pruebas sean más estables frente a los tiempos de carga de la aplicación.

## Ejecución de las pruebas

### 1. Instalar Python

Se requiere tener Python instalado en el equipo.

Puedes comprobar la instalación ejecutando:

```bash
python --version
```

### 2. Instalar las dependencias

Instala Selenium y Pytest utilizando `pip`:

```bash
pip install selenium pytest
```

### 3. Ejecutar las pruebas

Desde el directorio raíz del proyecto, ejecuta:

```bash
pytest main.py
```

También puedes ejecutar las pruebas mostrando información más detallada:

```bash
pytest -v main.py
```

## Resultado esperado

Al ejecutar las pruebas, Pytest mostrará en la terminal el resultado de cada caso de prueba.

Una ejecución exitosa debe mostrar que todas las pruebas fueron superadas:

```text
======================== test session starts ========================
...
========================= 9 passed in XX.XXs =========================
```

El tiempo de ejecución pueden variar dependiendo del entorno de ejecución.

## Consideraciones

Las pruebas utilizan Selenium WebDriver para controlar el navegador y requieren que el entorno esté correctamente configurado para ejecutar las pruebas automatizadas.

Algunas funcionalidades de Urban Routes pueden depender de los tiempos de respuesta de la aplicación. Por este motivo, se utilizan esperas explícitas para sincronizar las acciones de Selenium con el estado de la interfaz.

## Autor

Proyecto realizado como parte del **Sprint 9: Automatización de pruebas de la aplicación web**.
