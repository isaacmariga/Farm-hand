from re import L
from django.shortcuts import render
from django.shortcuts import render
from .models import Batch, Deaths, Expenses, Revenue

# Create your views here.



def home(request):
    projects = Batch.get_all() 

    return render(request, 'business/home.html',{'projects':projects})

def batch(request, id):
    deaths = Deaths.ind_by_batch(id) 
    d_sum =Deaths.death_sum(id)
    b_p = Batch.total_cost(id)
    t_e = Expenses.expense_sum(id)

    profit = b_p - t_e

    return render(request, 'business/batch.html',{'deaths':deaths, 'id':id, 'd_sum':d_sum, 'b_p':b_p, 't_e':t_e, 'profit':profit})


def charts(request):
    label= []
    data =[]

    queryset = Expenses.objects.order_by('-amount')[:5]
    for expense in queryset:
        data.append(expense.amount)
        label.append(expense.expense)
    return render(request, 'business/charts.html',{'labels':label, 'data':data }) 