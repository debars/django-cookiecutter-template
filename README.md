# Django Project Template

A refactored version of Django's standard project template.
The settings files are split into base.py, local.py, and production.py.
I've also added the directories that are standard to every Django project.
As a personal preference I place all of my static files and templates in a
public folder.

## Usage
```bash
$ django-admin.py startproject --template=https://github.com/MichaelCombs28/django-cookiecutter-template/archive/master.zip --extension=py,rst,html <project_name>
```	

## Manage Commands
```bash
$ ./manage.py runserver --settings=<project_name>.settings.local
```
