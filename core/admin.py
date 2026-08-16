from django.contrib import admin
from core.models import Employee,Department,AttendanceLog

# admin.site.register(Employee)
# admin.site.register(Department)
# admin.site.register(AttendanceLog)

class AttendanceLogInline(admin.TabularInline):
    model = AttendanceLog
    extra = 0

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','employee_type', 'employment_status', 'department')
    search_fields = ('first_name','last_name')

    inlines = [AttendanceLogInline]

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass

# @admin.register(AttendanceLog)
# class AttendanceAdmin(admin.ModelAdmin):
#     pass



