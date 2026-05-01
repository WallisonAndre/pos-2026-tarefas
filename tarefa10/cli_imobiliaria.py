import json

def carregar_dados():
    try:
        # Abre o arquivo JSON gerado na Tarefa 09
        with open("imobiliaria.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Erro: Arquivo imobiliaria.json não encontrado na pasta tarefa10.")
        return None

def detalhar_imovel(imovel):
    """Exibe todas as informações do imóvel de forma legível."""
    print("\n" + "="*50)
    print(f"DETALHES DO IMÓVEL ID: {imovel['id']}")
    print(f"Descrição: {imovel['descricao']}")
    print(f"Valor: R$ {imovel['valor']}")
    print("-" * 30)
    
    # Dados de Endereço
    end = imovel['endereco']
    num = end['numero'] if end['numero'] else "S/N"
    print(f"Localização: {end['rua']}, {num}")
    print(f"Bairro: {end['bairro']} | Cidade: {end['cidade']}")
    
    # Características Técnicas
    carac = imovel['caracteristicas']
    print(f"Área: {carac['tamanho']}m² | Quartos: {carac['quartos']} | Banheiros: {carac['banheiros']}")
    print("-" * 30)
    
    # Dados do Proprietário
    prop = imovel['proprietario']
    print(f"Proprietário: {prop['nome']}")
    if prop['email']:
        print(f"E-mail: {prop['email']}")
    if prop['telefones']:
        print(f"Telefones: {', '.join(prop['telefones'])}")
    print("="*50)

def menu():
    imoveis = carregar_dados()
    if not imoveis:
        return

    while True:
        print("\n--- MENU DE IMÓVEIS (Tarefa 10) ---")
        # Lista apenas os IDs e descrições para o menu
        for imovel in imoveis:
            print(f"[{imovel['id']}] - {imovel['descricao']}")
        
        print("[0] - Sair")
        
        escolha = input("\nDigite o ID para ver detalhes: ").strip()
        
        if escolha == '0':
            print("Encerrando programa...")
            break
            
        # Busca o imóvel pelo ID digitado
        encontrado = False
        for imovel in imoveis:
            if imovel['id'] == escolha:
                detalhar_imovel(imovel)
                encontrado = True
                break
        
        if not encontrado:
            print("\nID inválido! Escolha um número presente no menu.")
        
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    menu()