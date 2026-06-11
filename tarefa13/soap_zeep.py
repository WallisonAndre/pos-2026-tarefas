import zeep

wsdl_url = "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"

client = zeep.Client(wsdl=wsdl_url)

while True:
    print("\n1 - Converter Número | 0 - Sair")
    opcao = input("Escolha uma opção: ").strip()
    
    if opcao == "0":
        print("Saindo...")
        break
        
    if opcao == "1":
        numero_input = input("Digite um número inteiro: ").strip()
        
        if not numero_input.isdigit():
            print("Por favor, digite apenas números inteiros.")
            continue
            
        numero = int(numero_input)
        
        result = client.service.NumberToWords(ubiNum=numero)
        

        print(f"Número digitado: {numero}")
        print(f"Por extenso (inglês): {result.strip()}")
    else:
        print("Opção inválida!")