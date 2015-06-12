#!/bin/bash

python manage.py loaddata fixtures/contenttypes.json 
python manage.py loaddata fixtures/auth.json 
python manage.py loaddata fixtures/protolib.json 
