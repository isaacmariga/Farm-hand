from django import forms
from .models import Batch, Deaths, Expenses, Revenue, Customers, ExpenseGroup, ExpenseDetails

class BatchForm(forms.ModelForm):
  class Meta:
    model=Batch
    exclude=['user']



class DeathsForm(forms.ModelForm):
  class Meta:
    model=Deaths
    exclude=['batch']

class ExpensesForm(forms.ModelForm):
  class Meta:
    model=Expenses
    exclude=['batch']
class ExpenseGroupForm(forms.ModelForm):
  class Meta:
    model=ExpenseGroup
    exclude=['batch']
class ExpenseDetailsForm(forms.ModelForm):
  class Meta:
    model=ExpenseDetails
    exclude=['batch']

class RevenueForm(forms.ModelForm):
  class Meta:
    model=Revenue
    exclude=['batch']
    Widgets = { 'customer' : forms.CheckboxSelectMultiple() ,}


class CustomersForm(forms.ModelForm):
  class Meta:
    model=Customers
    exclude=['batch']