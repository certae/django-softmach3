#!/bin/bash

#  Tener en cuenta q al crear una app nueva los contettypes pueden varias y asi todos los permisos 

#  Borrar datos 
tar -zcvf "db/db-$(date +"%Y%m%d_%H%M%S").tar.gz" db/db.sqlite3


# Actualiza la db 
./dosyncdb.sh 
./dodumpdata.sh 

# Borra 
rm db/db.sqlite3
find . -name __pycache__  -type d -exec rm -r {} +
find . -name migrations  -type d -exec rm -r {} +

# Crear la db 
./dosyncdb.sh 

# Borrar contenido de las tablas 
python manage.py sqlflush | python manage.py dbshell

# Crear los datos 
./doloaddata.sh

# python ./manage.py createsuperuser
# python manage.py createinitialrevisions