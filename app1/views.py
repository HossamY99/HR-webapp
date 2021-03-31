from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import CreateEmployeeForm, SearchForm
from .models import Employee
from django.shortcuts import redirect


def index(request):
    return render(request, 'index.html')


def add_employee(request):
    if request.method == 'POST':
        form = CreateEmployeeForm(request.POST)
        if form.is_valid():
            employeeform = form.cleaned_data
            id = employeeform['Employee_id']
            name = employeeform['Employee_name']
            email = employeeform['email']
            photo = employeeform['photo']
            employee_department = employeeform['Employee_department']
            absences = employeeform['number_absences']
            overtime = employeeform['number_overtime']
            years = employeeform['years_of_work']
            salary = employeeform['salary']
            Employee.objects.create(Employee_id=id, Employee_name=name, email=email, photo=photo,
                                    Employee_department=employee_department, number_absences=absences,
                                    number_overtime=overtime, years_of_work=years, salary=salary)
            return render(request, 'index.html')
    else:
        form = CreateEmployeeForm()
    S = Employee.objects.all()
    return render(request, 'add_employee.html', {'form': form, 'S': S})


# def add_course(request):
#    if request.method == 'POST':
#        form = CreateCourseForm(request.POST)
#        if form.is_valid():
#            courseform = form.cleaned_data
#            Student_id = courseform['Student_id']
#            Course_id = courseform['Course_id']
#            Semester = courseform['Semester']
#            Number_of_credits = courseform['Number_of_credits']
#            Grade = courseform['Grade']
#            Course_Taken.objects.create(Student_id=Student_id, Course_id=Course_id, Semester=Semester,
#                                        Number_of_credits=Number_of_credits, Grade=Grade)
#            print(Student_id.Student_id)
#
#            listing = Course_Taken.objects.filter(Student_id=Student_id)
#            summ = 0.0
#            credits = 0
#            for l in listing:
#                print(Student_id)
#                summ = summ + l.Grade * l.Number_of_credits
#                credits = credits + l.Number_of_credits
#            avg = summ / credits
#            for e in Student.objects.all():
#                e.gpa = 20
#                print("im here")
#                if e.Student_id == Student_id.Student_id:
#                    print("here")
#                    e.gpa = avg
#                    e.save()
#                    print("changed")
#            return render(request, 'index.html')
#    else:
#        for e in Student.objects.all():
#            e.gpa = 20
#            e.save()
#        form = CreateCourseForm()
#    S = Course_Taken.objects.all()
#    return render(request, 'add_course.html', {'form': form, 'S': S})


def list(request):
    allemps=Employee.objects.all()
    return render(request, 'emplist.html', {'allemps': allemps})


def details(request, emp_id):
    res = Employee.objects.filter(Employee_id=emp_id).first()
    if res:
        return render(request, 'details.html', { 'emp': res})
    else:
        return HttpResponse("<h1> something went wrong searching for id"+str(emp_id)+"</h1>")



def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)

        if form.is_valid():
            empform = form.cleaned_data
            empname = empform['Employee_name']

            res = Employee.objects.filter(Employee_name__startswith=empname)
            if len(res) != 0:
                A = res
                print("here")
                print(A)
            try:
                return render(request, 'search_emp.html', {'form': form, 'A': A})
            except:
                errorstring = "employee not found"
                return render(request, 'search_emp.html', {'form': form, 'error': errorstring})
                # return redirect('/report_student', 'error': errorstring)
                # return HttpResponse("user not found")

    else:
        form = SearchForm()
    return render(request, 'search_emp.html', {'form': form})
