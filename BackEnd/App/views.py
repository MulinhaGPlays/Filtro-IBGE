from App.Library.Method import Method
from App.models import Departments, Employees
from App.serializers import DepartmentSerializer, EmployeeSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def departmentApi(request, id=None):
    return Method(request, id, Departments, DepartmentSerializer, 'DepartmentID')