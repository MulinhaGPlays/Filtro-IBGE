from App.models import Departments, Employees
from rest_framework import serializers


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departments
        fields =('__all__')
        

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees
        fields =('__all__')