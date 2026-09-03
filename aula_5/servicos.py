def cadastrar_tarefa(tarefas, titulo, descricao, prioridade, classe_tarefa):
    nova_tarefa = classe_tarefa(titulo, descricao, prioridade)
    tarefas.append(nova_tarefa)
    return nova_tarefa

def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    for indice, tarefa in enumerate(tarefas, start=1):
        print(f"{indice}. {tarefa.exibir_resumo()}")

def filtrar_por_situacao(tarefas, situacao):
    return [tarefa for tarefa in tarefas if tarefa.situacao == situacao]