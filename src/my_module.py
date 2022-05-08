from src import class_hotel

# dados: [0]tipo_de_cliente, [1]data_inicial, [2]data_do_meio, [3]data_final
def get_cheapest_hotel(number):
    # Filtra o input e o adapta para um formato mais legível ao programa
    number = number.replace(",", "").replace(":", "")
    dados = number.split()
    # Cria objetos do tipo Hotel
    lakewood = class_hotel.Hotel("Lakewood", 3, [110, 90], [80, 80])
    bridgewood = class_hotel.Hotel("Bridgewood", 4, [160, 60], [110, 50])
    ridgewood = class_hotel.Hotel("Ridgewood", 5, [220, 150], [100, 40])
    # Cria um dicionário que armazenará o preço total das estadias
    soma_precos = {
        lakewood : 0,
        bridgewood : 0,
        ridgewood : 0
    }
    
    # Faz a soma e guarda no dicionário
    for i in range(len(soma_precos)):
        soma_precos[lakewood] += lakewood.calcular_preco(dados[0], dados[i+1])
        soma_precos[bridgewood] += bridgewood.calcular_preco(dados[0], dados[i+1])
        soma_precos[ridgewood] += ridgewood.calcular_preco(dados[0], dados[i+1])
    
    # Dirá qual o hotel mais barato pelo valor guardado no dicionário
    if((soma_precos[lakewood] < soma_precos[bridgewood]) and (soma_precos[lakewood] < soma_precos[ridgewood])):
        cheapest_hotel = lakewood.nome
    elif((soma_precos[bridgewood] < soma_precos[lakewood]) and (soma_precos[bridgewood] < soma_precos[ridgewood])):
        cheapest_hotel = bridgewood.nome
    # Significa que ou Ridgewood é o mais barato, ou que todos tem valores iguais
    # Neste caso, Ridgewood tem a melhor classificação entre eles
    else:
        cheapest_hotel = ridgewood.nome
    
    return cheapest_hotel
