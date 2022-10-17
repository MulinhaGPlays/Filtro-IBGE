from App import views
from django.urls import path

urlpatterns = [
    path('department', views.DepartmentApi),
    path('department/', views.DepartmentApi),
    path(f'department/<int:id>', views.DepartmentApi),
    
    path('employ', views.EmployApi),
    path('employ/', views.EmployApi),
    path(f'employ/<int:id>', views.EmployApi),
]