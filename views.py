# Создание обработчика
# ====================
from django.http import HttpResponse
from django.shortcuts import render


def handler(request):
    context = "Hello, World!"
    return HttpResponse(context)


def index(request):
    context = "Hello, World!"
    # Возвращаем html страницу index
    return render(request, 'path/index.html', {'text': context})