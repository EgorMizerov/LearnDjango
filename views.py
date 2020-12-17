# Создание обработчика
# ====================
from django.http import HttpResponse

def handler(request):
    context = "Hello, World!"
    return HttpResponse(context)