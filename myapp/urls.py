from django.urls import path
from .views import funcao, cristina
urlpatterns = [
    path('maria', funcao),
    path('cristina', cristina)
]
