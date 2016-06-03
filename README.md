# Proyecto-Django
nicoblog con html y django
Recordatorio para ejecutar:
workon blog(o el workon creado)
python manage.py runserver

Recordatorio de django y como ejecutar:

#cuando modifique models

python manage.py makemigrations
python manage.py migrate

	#primera vez

sudo apt-get install python-pip

sudo pip install virtualenvwrapper

export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
export VIRTUALENVWRAPPER_SCRIPT=/usr/local/bin/virtualenvwrapper.sh
source /usr/local/bin/virtualenvwrapper.sh

(CREO) para crear un virtualEnv : mkvirtualenv MiNombre

workon MiNombre (entras al virtualEnv) 
(y pip install django si es que ya no lo hice)

django-admin.py startproject mysite

cd mysite

python manage.py runserver PUERTOSSIO


	#Otras veces

*source /usr/local/bin/virtualenvwrapper.sh*
workon MiNombre
cd mysite
python manage.py runserver PUERTOSSIO

	#Otras Cosas

python manage.py //Muestra todos los comandos disponibles
python manage.py startapp
python manage.py syncdb
python manage.py migrate
python manage.py runserver

	#Para que no haya que poner source siempre

sudo nano /home/TUUSUARIO/.bashrc
agregar en la ultima linea:
	source /usr/local/bin/virtualenvwrapper.sh
asi ya no hay que ponerla cada vez que se inice el proyecto.
