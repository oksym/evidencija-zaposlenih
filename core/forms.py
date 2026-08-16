from django import forms
from core.models import Employee,AttendanceLog

#ima mnogo polja u modelu pa sam izabrao modelforms
class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields= "__all__"

# class AttendanceLogForm(forms.ModelForm):
#     class Meta:
#         model=AttendanceLog
#         fields="__all__"