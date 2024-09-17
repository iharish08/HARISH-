from django.shortcuts import render, get_object_or_404
from .models import Employee

# View for listing all employees
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})

# View for individual employee details
def employee_details(request, id):  # Use 'id' to match the URL pattern
    employee = get_object_or_404(Employee, id=id)  # Fetch employee by 'id'
    return render(request, 'employees/employee_details.html', {'employee': employee})
