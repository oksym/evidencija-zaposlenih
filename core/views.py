from multiprocessing import context

from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from core.models import Employee, Department
from core.forms import EmployeeForm
from django.views.generic.edit import CreateView

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


def add_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = EmployeeForm()
    return render(request, 'employee_form.html', context={'form':form})

def edit_employee_profile(request,id):
    employee=get_object_or_404(Employee,id=id)
    if request.method=="POST":
        form= EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect("emp_detail",id=employee.id)
    else:
        form=EmployeeForm(instance=employee)
    return render(request, 'employee_form.html', context={'form':form, 'employee':employee})

def delete_employee_profile(request,id):
    employee=get_object_or_404(Employee, id=id)
    if request.method=="POST":
        employee.delete()
        return redirect("emp_list")
    return render(request, 'delete_confirm.html',context={'employee':employee})

def search_employee(request):
    query=request.GET.get('q')
    if query:
        employees=Employee.objects.filter(Q(first_name__icontains=query)|Q(last_name__icontains=query))
    else:
        employees=Employee.objects.all()
    return render(request, 'search_employee.html',context={'query':query,'employees':employees})

















