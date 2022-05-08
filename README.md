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

## Observações

A versão atual do programa foi feita especificamente para lidar com apenas os três hotéis citados anteriormente.
Assim sendo, para expandir este programan no futuro, de forma que ele possa analisar e comparar os preços de **n** hotéis
em estadias de durações diversas, seria necessário uma significante reformulação no módulo responsável (My_Module.py).

Meus pensamentos sobre como eu faria essa expansão se encontram no arquivo [Futuras_Expansões](Futuras_Expansões.md) na raíz do repositório.

