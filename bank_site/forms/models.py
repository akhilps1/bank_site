from django.db import models

# Create your models here.

class AccountForm(models.Model):
    full_name = models.CharField(max_length=250)
    user_age = models.IntegerField()
    user_dob = models.DateField()
    user_gender = models.CharField(max_length=250)
    user_email = models.EmailField()
    user_phone_no = models.IntegerField()
    user_address = models.TextField()
    district = models.CharField(max_length=250)
    branch = models.CharField(max_length=250)
    debit_card = models.BooleanField(default=False)
    credit_card = models.BooleanField(default=False)
    cheque_book = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"Name: {self.full_name}"