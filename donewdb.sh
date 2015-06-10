rm db/db.sqlite3
find . -name __pycache__  -type d -exec rm -r {} +
find . -name migrations  -type d -exec rm -r {} +

python ./manage.py makemigrations 
python ./manage.py makemigrations protoLib
python ./manage.py migrate 
python ./manage.py migrate protoLib
python ./manage.py createsuperuser

