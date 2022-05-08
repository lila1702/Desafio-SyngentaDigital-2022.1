# Expansão do Projeto 📂

Como mencionado no [README](README.md), o projeto no estado atual em que se encontra foi feito especificamente
para lidar apenas com os três hotéis propostos pelo desafio.

Uma expansão iria incluir as seguintes funcionalidades:

- Adicionar um número indefinido de hotéis;
- Marcar a data inicial da viagem e a data final da viagem;
- Comparar os preços totais da estadia entre todos os hotéis;
- Em casos de empate no preço, comparar todas as classificações entre si.

## Como eu faria isso?

Primeiramente, seria recomendado a utilização de alguma forma de banco de dados para receber
os hotéis que o programa poderia utilizar de referência. Assim, não seria necessário o uso de classes para
guardar as informações de cada hotel.

Para este exemplo, o banco de dados é uma matriz bidimensional, que através de laço(s) *for*, poderia ir
comparando cada preço, de acordo com o tipo de cliente e com o dia da semana.

| Nome Hotel   | Classificação | Preço Regular - Dia Útil | Preço Regular - Fim de Semana | Preço Reward - Dia Útil | Preço Reward - Fim de Semana |
|--------------|---------------|--------------------------|-------------------------------|-------------------------|------------------------------|
| Lakewood     |       3       |         110              |              90               |             80          |               80             |
| Bridgewood   |       4       |         160              |              60               |            110          |               50             |
| Ridgewood    |       5       |         220              |             150               |            100          |               40             |
|**Silverlake**|     **3**     |       **155**            |           **100**             |           **90**        |             **70**           |

```
tipo_cliente = ("Regular" ou "Reward")
datas = [data1, data2, ..., dataN)
cheapest_hotel = ["nome", 0, 100000000] # Nome, classificação e preço provisórios

for linha in range(len(hoteis)):
  # Pula a linha que indica o que é o que na tabela
  if(linha == 0):
    continue
  
  for coluna in range(len(hoteis)):
    classificacao = hoteis[linha][1]
    
    if(coluna == 0):
      continue
      
    if(tipo_cliente == "Regular" and coluna == 2 or tipo_cliente == "Regular" and coluna == 3):
      valor = calcular_preco_estadia(datas, hoteis[linha][2], hoteis[linha][3])
      
      if (valor < cheapest_hotel[2]):
        cheapest_hotel = [hoteis[linha][0], hoteis[1], valor]
      elif (valor == cheapest_hotel[1]):
        cheapest_hotel = [hoteis[linha][0], hoteis[1], valor] if classificacao > cheapest_hotel[1] else cheapest_hotel
      else:
        cheapest_hotel = cheapest_hotel
    
    else:
      valor = calcular_preco_estadia(datas, hoteis[linha][5], hoteis[linha][5])
      
      if (valor < cheapest_hotel[2]):
        cheapest_hotel = [hoteis[linha][0], hoteis[1], valor]
      elif (valor == cheapest_hotel[1]):
        cheapest_hotel = [hoteis[linha][0], hoteis[1], valor] if classificacao > cheapest_hotel[1] else cheapest_hotel
      else:
        cheapest_hotel = cheapest_hotel
```

Também criaria uma função que calcularia o valor total da estadia, de acordo com a data inicial e final.

```
calcular_preco_estadia(datas, preco_dia_util, preco_fim_de_semana):
  total = 0
  for dia in datas:
    if(dia.isoweekday() <= 5):
      total += preco_dia_util
    else:
      total += preco_fim_de_semana
  
  return total
```

Por fim, seria necessário algo para servir de interface que interage com o usuário.
Seria necessário um main.py com um loop, que recebe as datas de chegada e saída ao hotel, e opções de quebra do loop, caso o usuário deseje sair do programa.

Se fossemos continuar com o programa apenas com linhas de comando, ficaria algo como:
```
import datetime

while(True):
  print("Digite a data de chegada ao hotel:")
  data_chegada = input("dd/mm/aaaa: ")
  print("Digite a data de sáido do hotel:")
  data_saida = input("dd/mm/aaaa: ")
    
  try:
    if("/" in data_chegada or "/" in data_saida):
      data_chegada = data_chegada.replace("/", "")
      data_saida = data_saida.replace("/", "")
        
      data_chegada = datetime.datetime.strptime(data_chegada, "%d%m%Y")
      data_saida = datetime.datetime.strptime(data_saida, "%d%m%Y")
  except:
    print("Digite as datas novamente, no formato dd/mm/aaaa")
    continue
    
    print("Deseja continuar?")
    continuar = input("(S/N): ")
    continuar = continuar.upper()
    
    if(continuar == "N"):
  	  break
```

Caso fosse utilizar alguma interface gráfica, haveria adaptações, mas o princípio seguiria o mesmo.
