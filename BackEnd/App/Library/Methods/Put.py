from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.parsers import JSONParser
from rest_framework.status import HTTP_202_ACCEPTED, HTTP_304_NOT_MODIFIED


def Put(request, id, model, serializer, modelFieldID: str):
    print(model)
    model_data = JSONParser().parse(request)
    Model = get_object_or_404(model, DepartmentId=model_data[modelFieldID]) if id is None else get_object_or_404(model, pk=id)
    Serializer = serializer(Model, data=model_data)
    if Serializer.is_valid():
        Serializer.save()
        return JsonResponse("Atualizado com Sucesso!!", safe=False, status=HTTP_202_ACCEPTED)
    return JsonResponse("Falha ao Atualizar", safe=False, status=HTTP_304_NOT_MODIFIED)