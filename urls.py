# URL обработчик
from django.urls import path, include
from app import views
urlpatterns = [
    # Функция views
    path('path', views.home, name='home'), 
    
    # Использования другого url-оброботчика
    path('blog', include('blog.urls')),
]