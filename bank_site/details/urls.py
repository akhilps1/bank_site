from . import views
from django.urls import path


app_name = 'details'
urlpatterns = [
    path("", views.detail, name='detail'),

]