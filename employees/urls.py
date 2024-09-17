from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.employee_list, name='employee_list'),  # List view
    path('employee/<int:id>/', views.employee_details, name='employee_details'),  # Details view
]
