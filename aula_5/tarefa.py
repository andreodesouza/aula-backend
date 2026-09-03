class Tarefa:
    def __init__(self, titulo, descricao, prioridade):
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.situacao = "Pendente"

    def concluir(self):
        self.situacao = "Concluida"

    def exibir_resumo(self):
        return (
            f"Titulo: {self.titulo}"
            f"Prioridade: {self.prioridade}"
            f"Situação: {self.situacao}"

        )
