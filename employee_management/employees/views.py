from django.shortcuts import render, get_object_or_404
from .models import Employee

# List all employees
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})

# Show individual employee details
def employee_details(request, id):
    employee = get_object_or_404(Employee, id=id)
    return render(request, 'employees/employee_details.html', {'employee': employee})
