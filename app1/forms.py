from django.forms import ModelForm
from .models import Employee
from django import forms


# Create the form class.
class CreateEmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['Employee_id', 'Employee_name', 'email', 'photo', 'Employee_department', 'number_absences',
                  'number_overtime', 'years_of_work', 'salary']


# Create the form class.
# class CreateCourseForm(ModelForm):
#	class Meta:
#		model = Course_Taken
#		fields = ['Student_id', 'Course_id', 'Semester','Number_of_credits','Grade']

class SearchForm(forms.Form):
    Employee_name = forms.CharField()
