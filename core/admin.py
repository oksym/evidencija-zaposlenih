from django.contrib import admin
from core.models import Employee,Department

# admin.site.register(Employee)
# admin.site.register(Department)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','employee_type', 'employment_status', 'department')
    search_fields = ('first_name','last_name')


