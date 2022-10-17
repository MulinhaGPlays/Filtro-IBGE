from django.shortcuts import get_object_or_404
from App.models import Departments, Employees
from App.serializers import DepartmentSerializer, EmployeeSerializer
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.status import (
    HTTP_200_OK, HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST, HTTP_304_NOT_MODIFIED,
    HTTP_202_ACCEPTED
)

# Create your views here.

@csrf_exempt
def departmentApi(request, id=None):
    match request.method:
        case 'GET':
            many = True if id == None else False
            if id is None:
                departments = Departments.objects.all()
            else:
                departments = get_object_or_404(Departments, DepartmentId=id)
            departments_serializer = DepartmentSerializer(departments, many=many)
            return JsonResponse(departments_serializer.data, safe=False, status=HTTP_200_OK)
        case 'POST':
            if id is None:
                department_data = JSONParser().parse(request)
                departments_serializer = DepartmentSerializer(data=department_data)
                if departments_serializer.is_valid():
                    departments_serializer.save()
                    return JsonResponse("Adicionado com Sucesso!!", safe=False, status=HTTP_201_CREATED)
                return JsonResponse("Falha ao Adicionar", safe=False, status=HTTP_400_BAD_REQUEST)
            return JsonResponse("Este método não aceita o parâmetro ID", safe=False, status=HTTP_400_BAD_REQUEST)
        case 'PUT':
            department_data = JSONParser().parse(request)
            if id is None:
                department = get_object_or_404(Departments, DepartmentId=department_data['DepartmentId'])
            else:
                department = get_object_or_404(Departments, DepartmentId=id)
            departments_serializer = DepartmentSerializer(department, data=department_data)
            if departments_serializer.is_valid():
                departments_serializer.save()
                return JsonResponse("Atualizado com Sucesso!!", safe=False, status=HTTP_202_ACCEPTED)
            return JsonResponse("Falha ao Atualizar", safe=False, status=HTTP_304_NOT_MODIFIED)
        case 'DELETE':
            if id is not None:
                department = get_object_or_404(Departments, DepartmentId=id)
                department.delete()
                return JsonResponse("Deletado com Sucesso!!", safe=False, status=HTTP_202_ACCEPTED)
            return JsonResponse("Erro ao Deletar", safe=False, status=HTTP_400_BAD_REQUEST)
        case 'PATCH':
            return JsonResponse(request.method, safe=False, status=HTTP_400_BAD_REQUEST)
        case 'OPTIONS':
            return JsonResponse(request.method, safe=False, status=HTTP_400_BAD_REQUEST)
        case 'HEAD':
            return JsonResponse(request.method, safe=False, status=HTTP_400_BAD_REQUEST)
        case _:
            return JsonResponse(request.method, safe=False, status=HTTP_400_BAD_REQUEST)