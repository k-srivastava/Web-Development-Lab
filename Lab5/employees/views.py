from django.http import HttpResponse
from django.shortcuts import render

from .models import Employee


def index(request):
    return HttpResponse("Hello, world. You're at the employees index.")


def detail(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    is_eligible = employee.is_eligible_for_promotion()

    return render(request, 'employees/detail.html', {'is_eligible': is_eligible})
