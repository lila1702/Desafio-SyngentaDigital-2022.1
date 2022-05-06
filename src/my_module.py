import class_hotel

def get_cheapest_hotel(tipo_de_cliente, data_inicial, data_secundaria, data_final):   #DO NOT change the function's name
    lakewood = class_hotel.Hotel("Lakewood", 3, [110, 90], [80, 80])
    bridgewood = class_hotel.Hotel("Bridgewood", 4, [160, 60], [110, 50])
    ridgewood = class_hotel.Hotel("Ridgewood", 5, [220, 150], [100, 40])
    
    cheapest_hotel = "cheapest_hotel_name"
    
    soma_precos = {
        lakewood.nome : 0,
        bridgewood.nome : 0,
        ridgewood.nome : 0
    }
    
    '''
    for i in range(3):
        soma_precos[lakewood.nome] += (lakewood.calcular_preco_do_dia(tipo_de_cliente, data_inicial))
        soma_precos[bridgewood.nome] += (bridgewood.calcular_preco_do_dia(tipo_de_cliente, data_inicial))
        soma_precos[ridgewood.nome] += (ridgewood.calcular_preco_do_dia(tipo_de_cliente, data_inicial))
        
        data_inicial += timedelta(days = 1)
        
    for i in range(len(soma_precos)):
        if(soma_precos[lakewood.nome] < soma_precos[bridgewood.nome] and soma_precos[lakewood.nome] < soma_precos[ridgewood.nome]):
            cheapest_hotel = lakewood.nome
        elif(soma_precos[bridgewood.nome] < soma_precos[ridgewood.nome]):
            cheapest_hotel = bridgewood.nome
        else:
            cheapest_hotel = ridgewood.nome
    '''
    return cheapest_hotel

get_cheapest_hotel("Regular", "16Mar2009(mon)", "17Mar2009(tues)", "18Mar2009(wed)")