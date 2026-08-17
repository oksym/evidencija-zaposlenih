"""
URL configuration for evidencija_zaposlenih project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
# from core.views import employee_list,employee_detail,add_employee,edit_employee_profile,delete_employee_profile,departments_list,departments_detail,show_log,logs,search_employee
from core.views import home, EmployeeListView, EmployeeDetailView, AddEmployeeView, EditEmployeeView, DeleteEmployeeView,DepartmentListView,DepartmentDetailView, LogListView, LogsCreateView, SearchListView

urlpatterns = [
    path('', home, name='home'),
    # path('employee_list/', employee_list, name='emp_list'),
    path('employee_list/', EmployeeListView.as_view(),name='emp_list'),
    # path('employee_detail/<int:id>', employee_detail, name='emp_detail'),
    path('employee_detail/<int:pk>', EmployeeDetailView.as_view(), name='emp_detail'),
    # path('departments_list/', departments_list, name='dep_list'),
    path('departments_list/', DepartmentListView.as_view(), name='dep_list'),
    # path('departments_detail/<int:id>', departments_detail, name='dep_detail'),
    path('departments_detail/<int:pk>', DepartmentDetailView.as_view(), name='dep_detail'),
    # path('create_employee/', add_employee, name='create_emp'),
    path('create_employee/', AddEmployeeView.as_view(), name='create_emp'),
    # path('edit_employee/<int:id>', edit_employee_profile, name='edit_emp'),
    path('edit_employee/<int:pk>', EditEmployeeView.as_view(), name='edit_emp'),
    # path('delete_employee/<int:id>', delete_employee_profile, name='delete_emp'),
    path('delete_employee/<int:pk>', DeleteEmployeeView.as_view(), name='delete_emp'),
    # path('search_employee/', search_employee, name='search_emp'),
    path('search_employee/', SearchListView.as_view(), name='search_emp'),
    # path('logs/', logs, name='logs'),
    path('logs/', LogsCreateView.as_view(), name='logs'),
    # path('show_log/<int:id>', show_log, name='show_log' ),
    path('show_log/<int:pk>', LogListView.as_view(), name='show_log' ),
    path('login/', auth_views.LoginView.as_view(template_name='login.html',next_page="/" ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page="/"), name='logout'),
    path('admin/', admin.site.urls),
]
