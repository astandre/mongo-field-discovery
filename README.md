# Mongo Field Discovery

Esta herramienta permite recorrer los documentos de las diferentes colecciones de una base de datos Mongo.
Con el fin de determinar que estructura poseen los documentos. 
Exportanto los resultados en archivos CSV

## Requerimientos

Los requerimientos iniciales se encuentran en el archivo requirements.txt

Python +3.7

## Instalacion
Para instalar las dependencias necesarias usar el comando:

```shell script
pip install -r requirements.txt
```

## Uso

Configurar la conexion a la base de datos mongo:
```python
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
```

Definir que base de datos se va a explorar

```python
DB = "ocdb"
```

Definir la coleccion a explorar

```python
COLLECTION_NAME = "active"
```


Ejecutar la herramienta con el comando:

```shell script
python field_discovery
```