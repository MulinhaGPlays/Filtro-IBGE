from django.http.response import JsonResponse
from rest_framework.status import HTTP_400_BAD_REQUEST


def Others(request):
    return JsonResponse(f"O método {request.method} não está incluso", safe=False, status=HTTP_400_BAD_REQUEST)