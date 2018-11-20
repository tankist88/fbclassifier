from django.http import JsonResponse

from .models import Class
from .serializers import ClassSerializer

def get_classes(request):
    classes = ClassSerializer(
        Class.objects.all().order_by('-id'),
        many=True,
        context={'request':request}
    ).data
    return JsonResponse({'classes': classes})
