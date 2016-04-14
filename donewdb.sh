#!/bin/bash

#  Tener en cuenta q al crear una app nueva los contettypes pueden varias y asi todos los permisos 

# Actualiza la db 
# sh ./doMigrate.sh 
# sh ./dodumpdata.sh 

# Borra los datos 
rm db/db.sqlite3
find . -name __pycache__  -type d -exec rm -r {} +
find . -name migrations  -type d -exec rm -r {} +

# Crear la db 
sh ./doMigrate.sh 

# Borrar contenido de las tablas 
python manage.py sqlflush | python manage.py dbshell

# Crear los datos 
sh ./doloaddata.sh

# python ./manage.py createsuperuser
# python manage.py createinitialrevisions
