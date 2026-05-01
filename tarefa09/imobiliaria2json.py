import json
from xml.dom import minidom

def obter_texto(pai, tag):
    """Auxiliar para pegar o texto de uma tag filha."""
    elementos = pai.getElementsByTagName(tag)
    if elementos and elementos[0].firstChild:
        return elementos[0].firstChild.data
    return ""

def obter_telefones(proprietario_no):
    """Extrai todos os telefones de um proprietário."""
    tels = proprietario_no.getElementsByTagName("telefone")
    return [t.firstChild.data for t in tels if t.firstChild]

def converter():
    try:
        # Carrega o XML
        dom = minidom.parse("imobiliaria.xml")
        imoveis_xml = dom.getElementsByTagName("imovel")
        lista_final = []

        for i, imovel in enumerate(imoveis_xml):
            # Acessa os blocos filhos
            prop = imovel.getElementsByTagName("proprietario")[0]
            end = imovel.getElementsByTagName("endereco")[0]
            carac = imovel.getElementsByTagName("caracteristicas")[0]

            # Monta o dicionário seguindo a estrutura do seu XML
            dados = {
                "id": str(i + 1),
                "descricao": obter_texto(imovel, "descricao"),
                "proprietario": {
                    "nome": obter_texto(prop, "nome"),
                    "email": obter_texto(prop, "email"),
                    "telefones": obter_telefones(prop)
                },
                "endereco": {
                    "rua": obter_texto(end, "rua"),
                    "bairro": obter_texto(end, "bairro"),
                    "cidade": obter_texto(end, "cidade"),
                    "numero": obter_texto(end, "numero")
                },
                "caracteristicas": {
                    "tamanho": obter_texto(carac, "tamanho"),
                    "quartos": obter_texto(carac, "numQuartos"),
                    "banheiros": obter_texto(carac, "numBanheiros")
                },
                "valor": obter_texto(imovel, "valor")
            }
            lista_final.append(dados)

        # Salva o arquivo JSON
        with open("imobiliaria.json", "w", encoding="utf-8") as f:
            json.dump(lista_final, f, indent=4, ensure_ascii=False)
        
        print("Sucesso: Arquivo 'imobiliaria.json' gerado com os dados do XML!")

    except Exception as e:
        print(f"Erro na conversão: {e}")

if __name__ == "__main__":
    converter()