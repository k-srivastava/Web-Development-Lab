from django.http import HttpResponse

from .models import Student


def index(request):
    return HttpResponse("Hello, world. You're at the students index.")


def detail(request, student_id):
    return HttpResponse(f"You're looking at student {student_id}.")


def marks_percentage(request, student_id):
    student = Student.objects.get(pk=student_id)
    percentage = student.total_marks_percentage()

    return HttpResponse(f'Student {student.name} has {percentage:.2f}% marks.')
