from App import views
from django.urls import path

urlpatterns = [
    path('department/', views.departmentApi),
    path(f'department/<int:id>', views.departmentApi),
]