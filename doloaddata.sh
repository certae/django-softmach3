#!/bin/bash

python manage.py loaddata fixtures/contenttypes.json 
python manage.py loaddata fixtures/auth.json 
python manage.py loaddata fixtures/protolib.json 
python manage.py loaddata fixtures/protoExt.json 
python manage.py loaddata fixtures/prototype.json 
python manage.py loaddata fixtures/rai01ref.json 
