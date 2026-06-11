import requests
from xml.dom.minidom import parseString

url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"
headers = {'Content-Type': 'text/xml; charset=utf-8'}

while True:
    print("\nDigite 1 para Nome, 2 para Capital, 3 para Moeda ou 0 para Sair")
    opcao = input("Escolha uma opção: ").strip()

    if opcao == "0":
        print("Saindo...")
        break

    if opcao in ["1", "2", "3"]:
        country_code = input("Digite o código do país (ex: BR): ").strip().upper()
        
        if opcao == "1":
            payload = f"""<?xml version="1.0" encoding="utf-8"?>
            <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                <soap:Body>
                    <CountryName xmlns="http://www.oorsprong.org/websamples.countryinfo">
                        <sCountryISOCode>{country_code}</sCountryISOCode>
                    </CountryName>
                </soap:Body>
            </soap:Envelope>"""
            response = requests.request("POST", url, headers=headers, data=payload)
            if response.status_code == 200:
                resultado = parseString(response.text).documentElement.getElementsByTagName("m:CountryNameResult")[0].firstChild.nodeValue
                print("-> O nome do país é: " + resultado)

        elif opcao == "2":
            payload = f"""<?xml version="1.0" encoding="utf-8"?>
            <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                <soap:Body>
                    <CapitalCity xmlns="http://www.oorsprong.org/websamples.countryinfo">
                        <sCountryISOCode>{country_code}</sCountryISOCode>
                    </CapitalCity>
                </soap:Body>
            </soap:Envelope>"""
            response = requests.request("POST", url, headers=headers, data=payload)
            if response.status_code == 200:
                resultado = parseString(response.text).documentElement.getElementsByTagName("m:CapitalCityResult")[0].firstChild.nodeValue
                print("-> A capital do país é: " + resultado)

        elif opcao == "3":
            payload = f"""<?xml version="1.0" encoding="utf-8"?>
            <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                <soap:Body>
                    <CountryCurrency xmlns="http://www.oorsprong.org/websamples.countryinfo">
                        <sCountryISOCode>{country_code}</sCountryISOCode>
                    </CountryCurrency>
                </soap:Body>
            </soap:Envelope>"""
            response = requests.request("POST", url, headers=headers, data=payload)
            if response.status_code == 200:
                resultado = parseString(response.text).documentElement.getElementsByTagName("m:sISOCode")[0].firstChild.nodeValue
                print("-> O código da moeda é: " + resultado)
    else:
        print("Opção inválida!")