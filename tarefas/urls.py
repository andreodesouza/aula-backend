from django.urls import path
from tarefas import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("tarefas/", views.lista_tarefas, name="lista_tarefas"),
]