import datetime

class Hotel:
    def __init__(self, nome_hotel, classificacao, taxas_regulares, taxas_rewards) -> None:
        self.nome = nome_hotel
        self.classificacao = classificacao
        # Recebe uma lista com os valores de taxas disponíveis, índice 0 = dia útil, 1 = fim de semana
        self.taxas_regulares = taxas_regulares
        self.taxas_rewards = taxas_rewards

    # Retornará o preço condizente com a data especificada e o tipo de cliente
    def calcular_preco(self, tipo_de_cliente, data_input):
        # Converte string que representa uma data em um Tipo Data
        try:
            data = datetime.datetime.strptime(data_input, "%d%b%Y(%a)")
        except: # Como há inputs onde o dia da semana não são como o Datetime aceita ele...
            indice_problematico = data_input.rfind(data_input[-2]) # Reconhece a letra problemática (a penúltima)
            data_input = data_input[:indice_problematico] + data_input[indice_problematico+1:] # Retira-a
            data = datetime.datetime.strptime(data_input, "%d%b%Y(%a)")
        
        # Verifica se a data ocorre em um dia útil
        if(data.isoweekday() <= 5):
            if(tipo_de_cliente == "Regular"):
                return self.taxas_regulares[0]
            else: # (tipo_de_cliente == "Reward")
                return self.taxas_rewards[0]
        
        # Se não for em dia útil, é em dia de fim de semana
        else:
            if(tipo_de_cliente == "Regular"):
                return self.taxas_regulares[1]
            else: # (tipo_de_cliente == "Reward")
                return self.taxas_rewards[1]

