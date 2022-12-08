from django.shortcuts import render,redirect
from django.contrib import messages
from .models import AccountForm


# Create your views here.


def open_account(request):

    if request.method == 'POST':

        full_name = request.POST.get('fname')
        user_age = request.POST.get('age')
        user_dob = request.POST.get('dob')
        user_gender = request.POST.get('gender')
        user_email = request.POST.get('email')
        user_phone_no = request.POST.get('phone_no')
        user_address = f"{request.POST.get('address')}, {request.POST.get('address2')}"
        district = request.POST.get('select1')
        branch = request.POST.get('select2')
        debit_card = request.POST.get('debit')
        credit_card = request.POST.get('credit')
        cheque_book = request.POST.get('cheque')

        if debit_card == 'True':
            debit_card = True
        else:
            debit_card = False

        if credit_card == 'True':
            credit_card == True
        else:
            credit_card = False
    
        if cheque_book == 'True':
            cheque_book = True
        else:
            cheque_book = False

        print(credit_card,debit_card,cheque_book)        

        if full_name and user_email and user_phone_no is not None:
            fomrm_data = AccountForm(
                full_name=full_name,
                user_age=user_age,
                user_dob=user_dob,
                user_gender=user_gender,
                user_email=user_email,
                user_phone_no=user_phone_no,
                user_address=user_address,
                district=district,
                branch=branch,
                debit_card=debit_card,
                credit_card=credit_card,
                cheque_book=cheque_book
                )
        else:
            messages.info(request, 'fill all required fields')
            return redirect('forms:open_account') 
        fomrm_data.save()
        return redirect('details:show_confermation')    
    return render(request, 'forms.html')

