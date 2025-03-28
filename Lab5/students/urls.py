from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:student_id>', views.detail, name='detail'),
    path('results/<int:student_id>', views.marks_percentage, name='results'),
]
