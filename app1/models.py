from django.db import models


# Create your models here.


class Employee(models.Model):
    Employee_id = models.IntegerField(primary_key=True)
    Employee_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    photo = models.CharField(max_length=200, null=True, blank=True)
    Employee_department = models.CharField(max_length=50)
    number_absences = models.IntegerField()
    number_overtime = models.IntegerField()
    years_of_work = models.IntegerField()
    salary = models.FloatField()

    # Employee_department_id = models.ForeignKey(Student, on_delete=models.CASCADE)

# class Department(models.Model):
#    Department_id = models.IntegerField(primary_key=True)
#    Department_name = models.IntegerField()
#    Number_of_employees = models.IntegerField()
