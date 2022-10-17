from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.status import HTTP_200_OK


def Get(id, model, serializer):
    many = True if id == None else False
    Model = model.objects.all() if id is None else get_object_or_404(model, pk=id)
    Serializer = serializer(Model, many=many)
    return JsonResponse(Serializer.data if Serializer.data != [] else "A lista está vazia", safe=False, status=HTTP_200_OK)