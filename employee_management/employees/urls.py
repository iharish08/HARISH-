from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.employee_list, name='employee_list'),
    path('employee/<int:id>/', views.employee_details, name='employee_details'),
]
