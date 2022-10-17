from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.status import HTTP_202_ACCEPTED, HTTP_400_BAD_REQUEST


def Delete(id, model):
    if id is not None:
        Model = get_object_or_404(model, pk=id)
        Model.delete()
        return JsonResponse("Deletado com Sucesso!!", safe=False, status=HTTP_202_ACCEPTED)
    return JsonResponse("Erro ao Deletar", safe=False, status=HTTP_400_BAD_REQUEST)