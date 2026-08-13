from django.db import models

class Department(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name
class Employee(models.Model):

    EMPLOYEE_TYPE=[
        ('full-time','Full-time'),('part-time', 'Part-time'),('intern','Intern')
    ]

    EMPLOYMENT_STATUS=[
        ('active', 'Active' ),('inactive', 'Inactive')
    ]

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    mobile_phone=models.CharField(max_length=20)
    employee_type=models.CharField(max_length=30,choices=EMPLOYEE_TYPE) #posto vec postoje  odeljenja ja sam umesto titula kojih bi bilo mnogo ovde stavio drugi podatak
    employment_date=models.DateField()
    salary = models.PositiveIntegerField()
    employment_status=models.CharField(max_length=10, choices=EMPLOYMENT_STATUS)
    department=models.ForeignKey(Department, on_delete=models.PROTECT, related_name='employees')
    #nisam siguran PROTECT ili DELETE, da li kad odeljenje se obrise to znaci i da su zaposleni otpusteni

    def __str__(self):
        return f"{self.first_name} {self.last_name}"