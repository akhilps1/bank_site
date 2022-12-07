from django.shortcuts import render

# Create your views here.


def open_account(request):
    return render(request, 'forms.html')