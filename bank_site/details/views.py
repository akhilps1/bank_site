from django.shortcuts import render,redirect
from forms.models import FormSubmitted
from django.contrib.auth.models import User


# Create your views here.


def detail(request):
    # submitted = False
    # user_name = User.objects.get(id=id)
    # form_submitted = FormSubmitted.objects.get(user_name=user_name)
    # if user_name == form_submitted.user_name:
    #     submitted = True
    #     print(submitted)
    return render(request, 'details.html')


def show_confermation(request):
    return render(request, 'confirm.html')