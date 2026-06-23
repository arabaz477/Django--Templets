from django.shortcuts import render, redirect
from StackApp.forms import EmployeeForm
from StackApp.models import Employee

def index(request):
    if request.method== 'POST':
        forms=EmployeeForm(request.POST)
        if forms.is_valid():
            try:
                forms.save()
                return redirect('/')
            except:
                pass
    emp=EmployeeForm()
    return render(request,'index.Html',{'data':emp})

def about(request):
    return render (request,'About.Html')

def home(request):
    return render (request,'home.Html')

def services(request):
    return render (request,'Services.Html')