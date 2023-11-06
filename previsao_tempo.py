import requests


def obter_previsao_do_tempo(uf):
    url = f"https://api.hgbrasil.com/weather?format=json-cors&key=15065193&city_name={uf}"  # Substitua "seu_api_key" pelo seu token da HG Brasil
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Erro ao obter dados da API")
        return None

def exibir_previsao_do_tempo(data):
    if data:
        print(f"Temperatura Atual: {data['results']['temp']}°C")
        print(f"Data e Hora da Consulta: {data['results']['time']}")
        print(f"Descrição do Tempo Atual: {data['results']['description']}")
        print(f"Está de Dia? {data['results']['is_day']}") 
        print(f"Umidade: {data['results']['humidity']}%")
        print(f"Velocidade do Vento: {data['results']['wind_speed']} km/h")
        print(f"Nascer do Sol: {data['results']['sunrise']}")
        print(f"Pôr do Sol: {data['results']['sunset']}")
        print(f"Condição de Tempo Atual: {data['results']['condition']}")

def main():
    uf = input("Digite a UF (Unidade Federativa): ")
    data = obter_previsao_do_tempo(uf)
    if data:
        exibir_previsao_do_tempo(data)

if __name__ == "__main__":
    main()
