from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from core.models import Employee, Department, AttendanceLog
from core.forms import EmployeeForm
from django.db.models import Q


# =========================
# HOME
# =========================
def home(request):
    employees=Employee.objects.all()
    departments= Department.objects.all()
    total_emp=len(employees)
    total_dep=len(departments)
    active=[]
    inactive=[]
    for employee in employees:
        status=employee.employment_status
        if status=='active':
            active.append(status)
        else:
            inactive.append(status)
    total_active=len(active)
    total_inactive = len(inactive)
    return render(request, 'home.html',context={'total_emp':total_emp,'total_dep':total_dep,'total_active':total_active,'total_inactive':total_inactive } )


# =========================
# EMPLOYEES
# =========================
@login_required
def employee_list(request):
    employees= Employee.objects.all()
    return render(request, 'employee_list.html', context={'employees':employees})

def employee_detail(request,id):
    # employee=Employee.objects.get(id=id)
    employee = get_object_or_404(Employee,id=id)
    return render(request, 'employee_detail.html',context={'employee':employee} )

@login_required
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


# =========================
# DEPARTMENTS
# =========================
@login_required
def departments_list(request):
    departments=Department.objects.all()
    return render(request,'departments_list.html', context={'departments':departments})

def departments_detail(request,id):
    department = get_object_or_404(Department,id=id)
    employees=department.employees.all()
    return render(request,'departments_detail.html',context={'employees':employees})


# =========================
# ATTENDANCE
# =========================

# def logs(request):
#     if request.method=="POST":
#         form = AttendanceLogForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form= AttendanceLogForm()
#     return render(request, 'employee_form.html',context={'form':form})

@login_required()
def logs(request):
    employees=Employee.objects.all()
    if request.method=="POST":
        employee_id= request.POST["empl"]
        employee = Employee.objects.get(id=employee_id)
        date=request.POST["date"]
        clock_in=request.POST["clock_in"]
        clock_out = request.POST["clock_out"]
        attendance= AttendanceLog(employee= employee,date=date,clock_in=clock_in,clock_out=clock_out)
        attendance.save()
        return redirect('home')
    return render(request, 'log_form.html',context={'employees':employees} )

def show_log(request,id):
    employee=Employee.objects.get(id=id)
    logs=employee.attendances.all()
    return render(request, 'logs_list.html', context={'logs':logs, 'employee':employee})



















