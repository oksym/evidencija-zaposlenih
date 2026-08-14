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
from django.urls import path
from core.views import employee_list, home, employee_detail, departments_list, departments_detail, add_employee, \
    edit_employee_profile, delete_employee_profile,search_employee

urlpatterns = [
    path('', home, name='home'),
    path('employee_list/', employee_list, name='emp_list'),
    path('employee_detail/<int:id>', employee_detail, name='emp_detail'),
    path('departments_list/', departments_list, name='dep_list'),
    path('departments_detail/<int:id>', departments_detail, name='dep_detail'),
    path('create_employee/', add_employee, name='create_emp'),
    path('edit_employee/<int:id>', edit_employee_profile, name='edit_emp'),
    path('delete_employee/<int:id>', delete_employee_profile, name='delete_emp'),
    path('search_employee/', search_employee, name='search_emp'),
    path('admin/', admin.site.urls),
]
