chamados = [
    {
        "id":1,
        "titulo": "Instalar Roteador",
        "prioridade":"Alta",
        "situacao":"Aberto".lower(),
        "acesso":"Rede",
    },
    {
        "id":2,
        "titulo":"Receber Pagamento",
        "prioridade":"Médio",
        "situacao":"Fechado".lower(),
        "acesso":"Financeiro",
    },
    {
        "id":3,
        "titulo":"Trocar Memória RAM",
        "prioridade":"Urgente",
        "situacao":"Fechado".lower(),
        "acesso":"Hardware",
    },
    {
        "id":4,
        "titulo":"Enviar E-mail do Pagamento",
        "prioridade":"Baixa",
        "situacao":"Fechado".lower(),
        "acesso":"Rede",
    },
    {
        "id":5,
        "titulo":"Instalar Televisão",
        "prioridade":"Alta",
        "situacao":"Aberto".lower(),
        "acesso":"Estoque",
    },

]

def buscar_chamados():
    for chamado in chamados:
        print(f"#{chamado['id']} - {chamado['titulo']}")
        print(f"Prioridade: {chamado['prioridade']}")
        print(f"Situação: {chamado['situacao']}")
        print(f"Acesso: {chamado['acesso']}")

def filtrar_chamados():
        
    situacao_desejada = input('Escolha a situação do chamado: [aberto/fechado]: ').lower()
    encontrou_chamado = False

    for chamado in chamados:    
        if chamado ['situacao'] == situacao_desejada:
            print(f"#{chamado['id']} - {chamado['titulo']}")
            encontrou_chamado = True
    if not encontrou_chamado:
        print('Nenhum chamado encontrado para a situação informada.')


def atualizacao():
    id_procurado = int(input('Digite o id: '))
    nova_situacao = input('Digite a nova situação: ')
    encontrou_chamado = False 

    for chamado in chamados:
        if chamado['id'] == id_procurado:
            chamado['situacao'] = nova_situacao
            encontrou_chamado = True
            print("Situação atualizada com sucesso")
            break
    if not encontrou_chamado:
        print("Chamado não encontrado")   

def menu():

    while True:

        print('1 - Buscar Chamados')
        print('2 - Filtrar Chamados')
        print('3 - Atualizar Chamados')

        opcao = int(input('Escolha uma opção: '))

        if opcao == 1:
            buscar_chamados()
            
        elif opcao == 2:
            filtrar_chamados()
            
        elif opcao == 3:
            atualizacao()
                
    
menu()