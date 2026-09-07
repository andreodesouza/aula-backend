from django.shortcuts import render

def inicio(request):
    return render(request, "tarefas/inicio.html")

def lista_tarefas(request):
    tarefas = [
        {
            "titulo": "Revisar URLs no Django",
            "prioridade": "Alta",
            "situacao": "Pendente",
        },
        {
            "titulo": "Criar template de listagem",
            "prioridade": "Média",
            "situacao": "Concluída",
        },
        {
            "titulo": "Construir Projeto",
            "prioridade": "Alta",
            "situacao": "Concluída",
        },
    ]
    contexto = {"tarefas": tarefas}
    return render(request, "tarefas/lista.html", contexto)
