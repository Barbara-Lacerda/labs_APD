tabela_telefonica = {
    "João": "1234-5678",
    "Maria": "9876-5432",
    "Pedro": "4567-8901",
    "Ana": "2345-6789",
}

def buscar_telefone(nome):
    if nome in tabela_telefonica:
        return tabela_telefonica[nome]
    else:
        return "Nome não encontrado"

def adicionar_telefone(nome, telefone):
    tabela_telefonica[nome] = telefone
    print(f"Nome {nome} foi adicionado: {telefone}",flush=True) # flush=true: garante que a saída seja exibida imediatamente

def remover_telefone(nome):
    if nome in tabela_telefonica:
        del tabela_telefonica[nome]
        print(f"Nome {nome} foi removido da tabela",flush=True)
    else:
        print(f"Nome {nome} não encontrado",flush=True)

if __name__ == "__main__":
    print("Número da Maria: ", buscar_telefone("Maria"))
    print("Número da Bárbara: ", buscar_telefone("Bárbara"))
    adicionar_telefone("Bárbara", "1111-2222")
    print("Número da Bárbara: ", buscar_telefone("Bárbara"))
    remover_telefone("Pedro")
    print("Número do Pedro: ", buscar_telefone("Pedro"))