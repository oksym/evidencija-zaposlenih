from django.shortcuts import render, get_object_or_404
from core.models import Employee, Department

def home(request):
    return render(request, 'home.html')

def employee_list(request):
    employees= Employee.objects.all()
    return render(request, 'employee_list.html', context={'employees':employees})

def employee_detail(request,id):
    # employee=Employee.objects.get(id=id)
    employee = get_object_or_404(Employee,id=id)
    return render(request, 'employee_detail.html',context={'employee':employee} )

def departments_list(request):
    departments=Department.objects.all()
    return render(request,'departments_list.html', context={'departments':departments})

def departments_detail(request,id):
    department = Department.objects.get(id=id)
    employees=department.employees.all()
    return render(request,'departments_detail.html',context={'employees':employees})




