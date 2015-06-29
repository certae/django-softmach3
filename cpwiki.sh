#!/bin/bash

cp -r /home/dario/tmp/wiki/proj /var/www/html/dokuwiki/data/pages
chown -R www-data:www-data /var/www/html/dokuwiki/data/pages/proj/** 
