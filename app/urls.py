from django.contrib import admin
from django.urls import path
from django.http import JsonResponse

def hello_view(resquest):
    return JsonResponse({'id': 1, 'name': 'Titanic', 'year': '1999'})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_view),
]
