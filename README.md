# 🍃 Desafio Syngenta Digital 🍃

O desafio proposto pela Syngenta Digital durante a Etapa 2 do
seu processo seletivo de Estágio de 2022.

## O desafio

Ele consiste em fazer um programa que calcula o preço de três estadias em certos períodos
em três hotéis distintos e vê qual o mais barato, de acordo com o tipo de cliente, Regular ou de Fidelidade (Reward).

Os hotéis são e seus preços são:

- Em dias úteis

| Tipo Cliente | Lakewood | Bridgewood | Ridgewood |
|--------------|----------|------------|-----------|
| Regular      |    110   |     160    |     220   |
| Reward       |     80   |     110    |     100   |


- Em fins de semana

| Tipo Cliente | Lakewood | Bridgewood | Ridgewood |
|--------------|----------|------------|-----------|
| Regular      |     90   |      60    |     150   |
| Reward       |     80   |      50    |      40   |

Em casos de empate, o fator que decidiria o escolhido é sua classificação.

| Lakewood | Bridgewood | Ridgewood |
|----------|------------|-----------|
|3 estrelas| 4 estrelas | 5 estrelas|

## Instalação

- [Python3](https://www.python.org)
- Terminal **Bash**
- PyTest
```
$ pip install -r requirements.txt
```
ou
```
$ pip3 install -r requirements.txt
```

## Rodar o Teste

```
$ py.test
```

## Por que utilizei Classes?

Transformar os hotéis em objetos de classe tipo Hotel serve para que haja uma forma fácil de me referir a qualquer dado
sobre aquele hotel específico, além de organizar o código em Informações Sobre os Hotéis x Comparar Preços.

Também poderia ter sido utilizado listas, tuplas ou dicionários (até porque já estaria usando dicionário em [My_Module](src/my_module.py)).
No entanto, listas e tuplas fazem uso de índices númericos, algo que seria ruim por facilitar erros na hora de me referir a algum deles (Ex: "Qual era o índice que tinha o preço de fidelidade do fim de semana mesmo?").

Listas e tuplas funcionam melhor quando são poucos índices, ou quando são utilizados em laços, onde a passagem por índices é automática (Como também é visto no [My_Module](src/my_module.py) quando o input do usuário (nesse caso, o PyTest) é recebido pela função e convertida numa lista chamada **dados**).

Dicionários funcionariam melhor, mas ainda assim, como são vários atributos para cada hotel, acabaria necessitando de uma lista/tupla
para guardá-los, onde o problema anterior retornaria. No entanto, ele funciona bem em sua forma mais simples, para guardar
um único valor relacionado a uma *key*, neste caso, para guardar o valor total da estadia em determinado hotel.

Assim sendo, tudo que é relacionado a alguma informação sobre o hotel, como nomes, preços ou classificações foi facilmente registrada pela
classe, e facilmente acessível pelo seu objeto.

## Mas e se quisessemos expandir o programa?

A versão atual do programa foi feita especificamente para lidar com apenas os três hotéis citados anteriormente.
Assim sendo, para expandir este programan no futuro, de forma que ele possa analisar e comparar os preços de **n** hotéis
em estadias de durações diversas, seria necessário uma significante reformulação no módulo responsável [My_Module](src/my_module.py).

Meus pensamentos sobre como eu faria essa expansão se encontram no arquivo [Futuras_Expansões](Futuras_Expansões.md) na raíz do repositório.
