#views.py
from django.shortcuts import render #Имопртируем функцию для рендера html файла 

def home(request):
    """Функция home для вывода страницы home.html"""
    return render(request,"home.html")