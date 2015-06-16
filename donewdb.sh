#!/bin/bash

#  Tener en cuenta q al crear una app nueva los contettypes pueden varias y asi todos los permisos 

#  Borrar datos 
tar -zcvf "db/db-$(date +"%Y%m%d_%H%M%S").tar.gz" db/db.sqlite3


# Actualiza la db 
python manage.py makemigrations 
python manage.py makemigrations protoLib
python manage.py makemigrations protoExt
python manage.py makemigrations prototype
python manage.py migrate 

python manage.py dumpdata --indent 2 contenttypes 	> fixtures/contenttypes.json 
python manage.py dumpdata --indent 2 auth 			> fixtures/auth.json 
python manage.py dumpdata --indent 2 protoLib 		> fixtures/protolib.json 
python manage.py dumpdata --indent 2 protoExt 		> fixtures/protoExt.json 
python manage.py dumpdata --indent 2 prototype 		> fixtures/prototype.json 

# Borra 
rm db/db.sqlite3
find . -name __pycache__  -type d -exec rm -r {} +
find . -name migrations  -type d -exec rm -r {} +

# Crear la db 
python manage.py makemigrations 
python manage.py makemigrations protoLib
python manage.py makemigrations protoExt
python manage.py makemigrations prototype
python manage.py migrate 

# Borrar contenido de las tablas 
python manage.py sqlflush | python manage.py dbshell

# Crear los datos 
python manage.py loaddata fixtures/contenttypes.json 
python manage.py loaddata fixtures/auth.json 
python manage.py loaddata fixtures/protolib.json 
python manage.py loaddata fixtures/protoExt.json 
python manage.py loaddata fixtures/prototype.json 

# python ./manage.py createsuperuser
# python manage.py createinitialrevisions