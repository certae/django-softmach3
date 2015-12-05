#!/bin/bash

mkdir fixtures 

python manage.py dumpdata --indent 2 contenttypes 	> fixtures/contenttypes.json 
python manage.py dumpdata --indent 2 auth 			> fixtures/auth.json 
python manage.py dumpdata --indent 2 protoLib 		> fixtures/protolib.json 
python manage.py dumpdata --indent 2 protoExt 		> fixtures/protoExt.json 
python manage.py dumpdata --indent 2 prototype 		> fixtures/prototype.json 
python manage.py dumpdata --indent 2 rai01ref 		> fixtures/rai01ref.json 

# python manage.py dumpdata --natural-foreign --natural-primary --indent 2 contenttypes > fixtures/contenttypes.json 

mkdir datascripts

python manage.py dumpscript  auth 			> datascripts/auth.py
python manage.py dumpscript  protoLib 		> datascripts/protolib.py
python manage.py dumpscript  protoExt 		> datascripts/protoExt.py
python manage.py dumpscript  prototype 		> datascripts/prototype.py
python manage.py dumpscript  rai01ref 		> datascripts/rai01ref.py

#  Db 
tar -zcvf "db/db-$(date +"%Y%m%d_%H%M%S").tar.gz" db/db.sqlite3

