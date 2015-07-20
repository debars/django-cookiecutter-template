# Django Project Template

A refactored version of Django's standard project template.
The settings files are split into base.py, local.py, and production.py.
I've also added the directories that are standard to every Django project.
As a personal preference I place all of my static files and templates in a
public folder.

## Usage
```bash
$ django-admin.py startproject --template=https://github.com/MichaelCombs28/django-cookiecutter-template/archive/master.zip --extension=py,rst,html,md,txt <project_name>
```

## Get started
```bash
$ cd <project_name> git init

# Edit license if you want an MIT license
$ sed -i s#'Michael Combs'#'Your Name'# LICENSE

$ git init
$ git remote add <your repo url>
$ git add .
$ git commit -m "initial commit"
$ git push -u origin master
```

## Manage Commands
```bash
$ chmod a+x manage.py
$ ./manage.py runserver --settings=<project_name>.settings.local
# or
$ export DJANGO_SETTINGS_MODULE=<project_name>.settings.local
# then
$ ./manage.py runserver
```


## Ubuntu 14.04 Dependancies
Before running <code>pip install -r requirements.txt</code> be sure to have these libraries:
```bash
$sudo apt-get install python-dev libffi-dev libpng12-dev libjpeg-dev nodejs npm libpq-dev \
libssl-dev postgresql postgresql-contrib

# I use coffee and less or sass/scss depending on project
$sudo npm install -g bower casperjs phantomjs less sass coffee yuglify
```
