#!/bin/bash

#  Tener en cuenta q al crear una app nueva los contettypes pueden varias y asi todos los permisos 

#  Borrar datos 
tar -zcvf "db/db-$(date +"%Y%m%d-%H%M%S").tar.gz" db/db.sqlite3

rm db/db.sqlite3
find . -name __pycache__  -type d -exec rm -r {} +
find . -name migrations  -type d -exec rm -r {} +

# Crear la db 
python manage.py makemigrations 
python manage.py makemigrations protoLib
python manage.py migrate 
python manage.py migrate protoLib

# Borrar contenido de las tablas 
python manage.py sqlflush | python manage.py dbshell

# Crear los datos 
python manage.py loaddata fixtures/contenttypes.json 
python manage.py loaddata fixtures/auth.json 
python manage.py loaddata fixtures/protolib.json 


# python ./manage.py createsuperuser
python manage.py createinitialrevisions