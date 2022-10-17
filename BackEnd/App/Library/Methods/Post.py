from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST


def Post(request, id, serializer):
    model_data = JSONParser().parse(request)
    if id is None:
        Serializer = serializer(data=model_data)
        if Serializer.is_valid():
            Serializer.save()
            return JsonResponse("Adicionado com Sucesso!!", safe=False, status=HTTP_201_CREATED)
        return JsonResponse("Falha ao Adicionar", safe=False, status=HTTP_400_BAD_REQUEST)
    return JsonResponse("Este método não aceita o parâmetro ID", safe=False, status=HTTP_400_BAD_REQUEST)