# intro to the django python framework

# CREATING YOUR FIRST PROJECT
	# $ django-admin startproject mysite
	# this will creat mysite directory in the directory that you ran the command in.
	# startproject command created the following:
		''' mysite/
				manage.py
				mysite/
					__init__.py
					settings.py
					urls.py
					wsgi.py
		'''
	# - mysite/
		# the outer mysite/ is just a container for your project. You can rename this to anything you want.
	# - manage.py
		# this is a command line utility that lets you interact with the Django project.
		# more on manage.py - https://docs.djangoproject.com/en/1.8/ref/django-admin/
	# - mysite/
		# the inner mysite/ directory is the actual Python package for your project. Its name 
		# is the Python package name you'll need to use import anything inside it(e.g mysite.urls)
	# - mysite/__init__.py
		# this is an empty file that tells Python that this directory shold be considered a Python package.
	# - mysite/settins.py
		# this is the settings/configurations for this Django project
		# - more on settings.py - https://docs.djangoproject.com/en/1.8/topics/settings/
	# - mysite/urls.py
		# the URL declaration for this Django project; a "table o contents" of your Dhango powerd site.
		# more on urls.py here - https://docs.djangoproject.com/en/1.8/topics/http/urls/
	# - mysite/wsgi.py
		#

