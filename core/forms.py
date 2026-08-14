from django import forms
from core.models import Employee
#ima mnogo polja u modelu pa sam izabrao modelforms
class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields= "__all__"