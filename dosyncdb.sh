#!/bin/bash

python ./manage.py makemigrations 
python ./manage.py makemigrations protoLib
python ./manage.py migrate 
