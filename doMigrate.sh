#!/bin/bash

# python manage.py makemigrations $1
python manage.py makemigrations protoLib
python manage.py makemigrations protoExt
python manage.py makemigrations prototype
python manage.py makemigrations rai01ref
python manage.py migrate 


