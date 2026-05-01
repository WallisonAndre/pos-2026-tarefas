from xml.dom import minidom

def carregar_dados():
    try:
        # Faz o parse do arquivo XML
        dom = minidom.parse("cardapio.xml")
        # Retorna a lista de elementos <prato>
        return dom.getElementsByTagName("prato")
    except FileNotFoundError:
        print("Erro: O arquivo 'cardapio.xml' não foi encontrado.")
        return []

def extrair_texto(elemento, tag_name):
    nos = elemento.getElementsByTagName(tag_name)
    if nos and nos[0].firstChild:
        return nos[0].firstChild.data
    return "N/A"

def exibir_menu(pratos):
    print("\n" + "="*30)
    print("       MENU DO DIA")
    print("="*30)
    for prato in pratos:
        id_prato = prato.getAttribute("id")
        nome = extrair_texto(prato, "nome")
        print(f"[{id_prato}] - {nome}")

def mostrar_detalhes(pratos, id_escolhido):
    for prato in pratos:
        if prato.getAttribute("id") == id_escolhido:
            nome = extrair_texto(prato, "nome")
            descricao = extrair_texto(prato, "descricao")
            preco = extrair_texto(prato, "preco")
            calorias = extrair_texto(prato, "calorias")
            tempo = extrair_texto(prato, "tempoPreparo")
            
            # Busca a lista de ingredientes
            ingredientes_nos = prato.getElementsByTagName("ingrediente")
            lista_ingredientes = [node.firstChild.data for node in ingredientes_nos if node.firstChild]

            print(f"\n>>> DETALHES DO PRATO: {nome.upper()} <<<")
            print(f"Descrição: {descricao}")
            print(f"Ingredientes: {', '.join(lista_ingredientes)}")
            print(f"Preço: R$ {preco}")
            print(f"Calorias: {calorias} kcal")
            print(f"Tempo de Preparo: {tempo}")
            return
    
    print("\nID inválido! Por favor, escolha um ID presente no menu.")

def main():
    pratos = carregar_dados()
    
    if not pratos:
        return

    while True:
        exibir_menu(pratos)
        escolha = input("\nDigite o ID do prato (ou 'sair'): ").strip()
        
        if escolha.lower() == 'sair':
            print("Encerrando programa...")
            break
            
        mostrar_detalhes(pratos, escolha)
        
        input("\nPressione Enter para voltar ao menu...")

if __name__ == "__main__":
    main()