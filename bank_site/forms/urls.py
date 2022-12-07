from . import views
from django.urls import path

app_name = 'forms'
urlpatterns = [
    path("", views.open_account, name='open_account'),

]