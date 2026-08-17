from multiprocessing import context

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from core.models import Employee, Department, AttendanceLog
from core.forms import EmployeeForm
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


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
# @login_required
# def employee_list(request):
#     employees= Employee.objects.all()
#     return render(request, 'employee_list.html', context={'employees':employees})
class EmployeeListView(LoginRequiredMixin,ListView):
    model=Employee
    template_name = 'employee_list.html'
    context_object_name = 'employees'


# def employee_detail(request,id):
#     # employee=Employee.objects.get(id=id)
#     employee = get_object_or_404(Employee,id=id)
#     return render(request, 'employee_detail.html',context={'employee':employee} )
class EmployeeDetailView(DetailView):
    model=Employee
    template_name = 'employee_detail.html'
    context_object_name = 'employee'


# @login_required
# def add_employee(request):
#     if request.method == "POST":
#         form = EmployeeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("home")
#     else:
#         form = EmployeeForm()
#     return render(request, 'employee_form.html', context={'form':form})
class AddEmployeeView(LoginRequiredMixin,CreateView):
    model = Employee
    template_name = 'employee_form.html'
    fields = "__all__"
    success_url = reverse_lazy("home")


# def edit_employee_profile(request,id):
#     employee=get_object_or_404(Employee,id=id)
#     if request.method=="POST":
#         form= EmployeeForm(request.POST, instance=employee)
#         if form.is_valid():
#             form.save()
#             return redirect("emp_detail",id=employee.id)
#     else:
#         form=EmployeeForm(instance=employee)
#     return render(request, 'employee_form.html', context={'form':form, 'employee':employee})
class EditEmployeeView(UpdateView):
    model = Employee
    template_name = 'employee_form.html'
    fields = "__all__"

    def get_success_url(self):
        return reverse_lazy(
            "emp_detail",
            kwargs={"pk": self.object.pk}
        )


# def delete_employee_profile(request,id):
#     employee=get_object_or_404(Employee, id=id)
#     if request.method=="POST":
#         employee.delete()
#         return redirect("emp_list")
#     return render(request, 'delete_confirm.html',context={'employee':employee})
class DeleteEmployeeView(DeleteView):
    model = Employee
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('emp_list')


# def search_employee(request):
#     query=request.GET.get('q')
#     if query:
#         employees=Employee.objects.filter(Q(first_name__icontains=query)|Q(last_name__icontains=query))
#     else:
#         employees=Employee.objects.all()
#     return render(request, 'search_employee.html',context={'query':query,'employees':employees})


class SearchListView(ListView):
    model = Employee
    template_name = 'search_employee.html'
    context_object_name = "employees"

    def get_queryset(self):
        query = self.request.GET.get("q")

        if query:
            return Employee.objects.filter(
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query)
            )

        return Employee.objects.all()

# =========================
# DEPARTMENTS
# =========================

# @login_required
# def departments_list(request):
#     departments=Department.objects.all()
#     return render(request,'departments_list.html', context={'departments':departments})
class DepartmentListView(LoginRequiredMixin, ListView):
    model = Department
    template_name = 'departments_list.html'
    context_object_name = 'departments'


# def departments_detail(request,id):
#     department = get_object_or_404(Department,id=id)
#     employees=department.employees.all()
#     return render(request,'departments_detail.html',context={'employees':employees})
class DepartmentDetailView(DetailView):
    model = Department
    template_name = 'departments_detail.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["employees"] = self.object.employees.all()
        return context

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

# @login_required()
# def logs(request):
#     employees=Employee.objects.all()
#     if request.method=="POST":
#         employee_id= request.POST["empl"]
#         employee = Employee.objects.get(id=employee_id)
#         date=request.POST["date"]
#         clock_in=request.POST["clock_in"]
#         clock_out = request.POST["clock_out"]
#         attendance= AttendanceLog(employee= employee,date=date,clock_in=clock_in,clock_out=clock_out)
#         attendance.save()
#         return redirect('home')
#     return render(request, 'log_form.html',context={'employees':employees} )
class LogsCreateView(LoginRequiredMixin,CreateView):
    model = AttendanceLog
    template_name = 'employee_form.html'
    fields = "__all__"
    success_url = reverse_lazy("home")


# def show_log(request,id):
#     employee=Employee.objects.get(id=id)
#     logs=employee.attendances.all()
#     return render(request, 'logs_list.html', context={'logs':logs, 'employee':employee})
class LogListView(DetailView):
    model = Employee
    template_name = 'logs_list.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["logs"]=self.object.attendances.all()


















