from src import class_hotel

# dados: [0]tipo_de_cliente, [1]data_inicial, [2]data_do_meio, [3]data_final
def get_cheapest_hotel(number):   #DO NOT change the function's name
    number = number.replace(",", "").replace(":", "") # Remove dois pontos e vírgula
    dados = number.split() # Divide a string em uma lista, cada elemento é separado por espaço em branco
    # Cria objetos do tipo Hotel
    lakewood = class_hotel.Hotel("Lakewood", 3, [110, 90], [80, 80])
    bridgewood = class_hotel.Hotel("Bridgewood", 4, [160, 60], [110, 50])
    ridgewood = class_hotel.Hotel("Ridgewood", 5, [220, 150], [100, 40])
    # Cria um dicionário que armazenará o preço total da estadia
    soma_precos = {
        lakewood.nome : 0,
        bridgewood.nome : 0,
        ridgewood.nome : 0
    }
    
    # Faz a soma e guarda no dicionário
    for i in range(3):
        soma_precos[lakewood.nome] += lakewood.calcular_preco(dados[0], dados[i+1])
        soma_precos[bridgewood.nome] += bridgewood.calcular_preco(dados[0], dados[i+1])
        soma_precos[ridgewood.nome] += ridgewood.calcular_preco(dados[0], dados[i+1])
    
    # Dirá qual o hotel mais barato pelo valor total da estadia guardada no dicionário
    if((soma_precos[lakewood.nome] < soma_precos[bridgewood.nome]) and (soma_precos[lakewood.nome] < soma_precos[ridgewood.nome])):
        cheapest_hotel = lakewood.nome
    elif((soma_precos[bridgewood.nome] < soma_precos[lakewood.nome]) and (soma_precos[bridgewood.nome] < soma_precos[ridgewood.nome])):
        cheapest_hotel = bridgewood.nome
    # Se chegar no else, significa que ou Ridgewood é o mais barato, ou que todos tem valores iguais
    # Neste caso, Ridgewood tem a melhor classificação entre eles
    else:
        cheapest_hotel = ridgewood.nome
    
    return cheapest_hotel