python manage.py dumpdata --indent 2 contenttypes 	> fixtures/contenttypes.json 
python manage.py dumpdata --indent 2 auth 			> fixtures/auth.json 
python manage.py dumpdata --indent 2 protoLib 		> fixtures/protolib.json 

# python manage.py dumpdata --natural-foreign --natural-primary --indent 2 contenttypes > fixtures/contenttypes.json 
