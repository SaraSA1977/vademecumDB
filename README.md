## isabella alvarez 
## camilo vanegas
## sara sanchez

# VademecumDB – API REST
Proyecto backend desarrollado en Flask para la gestión de un Vademécum de Optometría.
Permite administrar:
- Grupos farmacológicos
- Formas farmacéuticas
- Detalles de productos

Base de datos desarrollada en PostgreSQL y gestionada desde DBeaver.

# 1. Normalización y Diseño de Tablas
El archivo Vademécum fue normalizado hasta 3FN (Tercera Forma Normal).
Se separaron las entidades en:
## Tabla grupos
- id (PK)
- nombre
## Tabla forma_farmaceutica
- id (PK)
- nombre
## Tabla product_details
- id (PK)
- comercial_name
- concentracion
- notas
- id_grupo (FK → grupos.id)
- id_FF (FK → forma_farmaceutica.id)

Justificación:
- Eliminación de redundancia.
- Separación de dependencias funcionales.
- Uso de claves primarias y foráneas correctamente definidas.

# 2. Creación de Base de Datos en DBeaver

1. Abrir DBeaver
2. Crear nueva base de datos llamada: vademecumDB
3. Configurar conexión PostgreSQL
4. Validar conexión activa

# 3. Configuración de Variables de Entorno
Archivo .env (NO incluido en GitHub gracias a .gitignore)
Crear un archivo llamado .env en la raíz del proyecto y agregar:
DB_URL=postgresql://postgres:TU_PASSWORD@localhost:5432/vademecumDB
HOST=127.0.0.1
PORT=5000
JWT_SECRET_KEY=supersecretkey

## en el DB_URL se debe modificar TU_PASSWORD por la contraseña configurada en PostgreSQL (la misma que usas para ingresar desde pgAdmin o DBeaver)
El archivo `.gitignore` evita exponer credenciales.

# 4. Conexión a Base de Datos desde Python

La conexión se realiza mediante SQLAlchemy usando variables de entorno.

Se carga configuración con dotenv y se establece conexión modular en archivo separado.

La conexión fue validada mostrando el mensaje "Connected to DB OK" al iniciar el servidor.

# 5. Models SQLAlchemy
Se definieron los siguientes modelos:
- Grupo
- FormaFarmaceutica
- ProductDetails (con relaciones)

Ejemplo de relación:
- ProductDetails.id_grupo → ForeignKey a grupos.id
- ProductDetails.id_FF → ForeignKey a forma_farmaceutica.id

# 6. Creación de Tablas desde Python

Las tablas se crean utilizando:
db.create_all()
Con relaciones activas entre tablas.

# 7. Sistema HTTP Estandarizado
Las respuestas siguen estructura uniforme:
{
  "status": "success",
  "message": "Operación realizada correctamente",
  "data": {...}
}
En caso de error:
{
  "status": "error",
  "message": "Descripción del error",
  "errors": {...}
}

# 8. CRUD Completo
Se implementó CRUD para:
- grupos
- forma_farmaceutica
- product_details
Operaciones:
Create
Read
Update
Delete
Con manejo de errores e integridad referencial.

# 9. Configuración del Servidor

Archivo principal: app.py

- Registro de Blueprints
- Configuración CORS
- Variables de entorno
- Puerto configurable

Servidor ejecutado con: python app.py

# 10. Asociación de Rutas

Blueprints registrados correctamente:

/grupos
/ff
/products

Ejemplo:

DELETE http://localhost:5000/products/deleteProduct/1

# 11. Validación en Postman

## POST
las rutas para el metodo POST son las siguiente:
http://localhost:5000/grupos/createGrupo
http://localhost:5000/ff/createFF 
http://localhost:5000/products/createProduct 

A continuacion se anexaran capturas sobre como creamos las consultas

Captura:
![grupo creado](evidencias/grupo_post.png)
![ff creado](evidencias/ff_post.png)
![Producto Creado 1](evidencias/producto_creado1.png)


## PUT
las rutas para el metodo PUT son las siguiente:
http://localhost:5000/grupos/updateGrupo/1
http://localhost:5000/ff/updateFF/1 
http://localhost:5000/products/updateProduct/2 

Captura:
![Update grupo](evidencias/update_grupo.png)
![Update ff](evidencias/put_ff.png)
![Update pd](evidencias/put_pd.png)


## Gets
las rutas para el metodo getAll son las siguiente:
http://localhost:5000/grupos/getAll
http://localhost:5000/ff/getAll 
http://localhost:5000/products/getAll

Captura:
![GetAll grupos](evidencias/getAllgrupos.png)
![GetAll ff](evidencias/getAllff.png)
![GetAll products](evidencias/getAllproducts.png)


## Deletes
las rutas para el metodo DELETE son las siguiente:
http://localhost:5000/grupos/deleteGrupo/3 
http://localhost:5000/ff/deleteFF/3
http://localhost:5000/products/deleteProduct/2

el ultimo numero indica de que ID queremos borrar la informacion teniendo en cuenta que como hay una tabla que se relaciona con las otras dos no podemos eliminar algo de grupo o de FF si aun existe en la tabla products porque entonces nos dara error.

Captura:
![Delete grupo](evidencias/delete_grupo.png)
![Delete ff](evidencias/delete_ff.png)
![Delete ff](evidencias/delete_product.png)

## resultados esperados
![resultado grupo](evidencias/resultado_esperadogrupo.png)
![resultado ff](evidencias/resultado_esperadoff.png)
![resultado products](evidencias/resultado_esperado_products.png)


# Instrucciones para Ejecutar el Proyecto

1. Clonar repositorio

git clone https://github.com/TU_USUARIO/vademecumDB.git

2. Entrar al proyecto

cd vademecumDB

3. Crear la base de datos en PostgreSQL

4. Crear entorno virtual

python -m venv venv

5. Activar entorno

Windows:
venv\Scripts\activate

6. Instalar dependencias:
pip install flask flask-cors sqlalchemy psycopg2 python-dotenv.

7. Configurar archivo .env

8. Ejecutar servidor

python app.py

Servidor disponible en:

http://127.0.0.1:5000