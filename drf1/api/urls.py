from django.urls import path
from . import views

urlpatterns = [
    # use path function to set some endpoints and pass in the .get_data view
    path('', views.get_data),
    path('add/', views.add_item),
]