# drf-practice-1
Django Rest Framework Practice

- new directory
- python -m venv .venv
- source .venv/bin/activate
- pip install django
- pip install djangorestframework
- django-admin startproject <name>
- project settings.py, INSTALLED_APPS -> 'rest_framework',
- mkdir api in project root
- api -> touch __init__.py
- api -> views.py
	import Response
	import api_view
	getData, allow GET method, return dummy data as json
- api -> urls.py
	import path
	import views
	create urlpatterns list
	create '' path using getData view
- project urls.py
	import include
	connect root urls.py to api's urls.py
- *check output
	python manage.py runserver
- startapp base
- register base app in project settings.py
- base models.py -> add a model called item, with 2 attributes:
	with name
	and created
- makemigrations
- apply migrations with migrate
- shell to add data
	create 3 items
	*print items to confirm
	exit shell
- start up the server
- api -> serializers.py
	import serializers
	import Item
	class ItemSerializer
	inner meta class with 2 required attributes
- api -> views
	import Item
	import ItemSerializer
	delete dummy data
	in get_data:
		query all items from db
		serialize
		return serializer.data in reponse object
- *check output in browser
- add in one more endpoint to see how to add data with api
- api -> views
	create view add_item with post method allowed
	serialize request.data
	check if is_valid(), save
	return newly created item in response
- api -> urls
	create path for new endpoint called add/ and pass in add_item view 
- *checkout new endpoint in browser
	see 405 can't GET
	in content section replicate what a real request might look like in the frontend
	pass in object with name attribute
	post it
*checkout home route with new item
