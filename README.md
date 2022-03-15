# Clothesstore LATAM Prueba Técnica

***

### Requisitos:

Los paquetes que se requieren para correr la aplicación se encuentran en `requirements.txt`. Recomiendo utilizar el entorno virtual venv activandolo con el comando:
```
venv\Scripts\activate
```

Para instalar todos los paquetes necesarios una vez activado el entorno virtual se puede utilizar el comando:
```
pip install -r requirements.txt
```

Los paquetes se pueden instalar por separado también, con los más importantes para la aplicación siendo: `Flask`, `Pillow`, y `sqlite3`. 

### Cómo correr el proyecto:

1. Establecer la ubicación de la aplicación de Flask:
En windows:
```
set FLASK_APP=products.app
```
En linux:
```
export FLASK_APP=products.app
```

2. Crear el esquema de bases de datos (en el caso de ser necesario, ya que subí algunos datos de prueba):
```
python products/db.py
```

3. Correr el proyecto Flask:
```
flask run
```

> :exclamation: Se puede acceder a la API por medio de Heroku en: https://experimentality-prueba.herokuapp.com/ (Existen errores por el uso de sqlite)

***

### Documentación de la API

```
GET /products
```

Recupera todos los productos registrados actualmente.

```
POST /products
```

Crea un nuevo producto con sus imágenes.

```
GET /images
```

Recupera todas las imágenes registradas actualmente.

```
GET /most_searched/<int:amount>
```

Recupera los productos más buscados de acuerdo a una cantidad específica de productos, retornados en orden descendente desde mayor buscado a menor buscado.