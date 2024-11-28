# Backend para el aplicativo Catalog Store - grupo 02

## Descripción:

## Detalles:
- Uso del framework Flask, extendido con Marshmallow
- Uso del gestor de base de datos Postgresql
- Uso de render para desplegar proyecto

## Instalación:
- Descargamos el repositorio como .ZIP o con el siguiente comando:
```bash
git clone git@github.com:MiguelVaDu/dsm_g02_backend_CatalogStore.git
```

- Una vez instalado, nos dirigimos a la carpeta del proyecto importado
```bash
cd dsm_g02_backend_CatalogStore/
```

- Abrimos en nuestro editor de codigo e instalamos el entorno virtual por la terminal:
```bash
virtualenv venv
```

- En caso de no tener la librería *virtualenv*, instalamos con el siguiente comando:
```bash
pip install virtualenv
```

- Continuando con la instalación, activamos el entorno virtual:

### Para sistemas WINDOWS:
```cmd
venv\Scripts\activate
```

### Para sistemas LINUX:
```bash
source venv/bin/activate
```

- Con esto, instalamos los requerimientos del proyecto:
```bash
pip install -r requirements.txt
```

- Creamos un archivo .env para realizar la configuración de la base de datos, en el archivo debe ir lo siguiente:
```.env
USER = <nombre-del-usuario-de-la-base-de-datos>
PASSWORD = <contraseña-de-la-base-de-datos>
DATABASE = <nombre-de-la-base-de-datos>
HOST = <host-de-la-base-de-datos>
SERVER = postgresql
```

- Corremos el programa
```bash
python app.py
```
Contact
For any questions or assistance, please contact the following people:
- https://github.com/MiguelVaDu
