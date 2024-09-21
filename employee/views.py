from django.shortcuts import render
from .models import Employee , Position


def Employees(request):
    employee = Employee.objects.all()
    return render(request,'employees.html',{'employee':employee})



    


