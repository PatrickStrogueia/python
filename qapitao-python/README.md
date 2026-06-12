# QApitão - Python ⚓

Este repositório contém uma coleção de scripts práticos em Python voltados para o aprendizado de lógica de programação, estruturas de dados, funções e programação orientada a objetos (POO). É um excelente ponto de partida para quem está dando os primeiros passos no desenvolvimento ou na automação de testes (QA) utilizando Python.

---

## 📂 Estrutura do Projeto

Os arquivos estão organizados de forma incremental, partindo dos conceitos mais simples até a estruturação de classes e lógica orientada a objetos.

### Conceitos Básicos e Sintaxe

*   **[hello.py](./hello.py)**: O tradicional ponto de partida ("Hello World") para testar o ambiente.
*   **[variaveis.py](./variaveis.py)**: Exemplos de declaração de variáveis e tipos básicos de dados.
*   **[operadores.py](./operadores.py)**: Demonstração de operadores aritméticos e de comparação.
*   **[inputs.py](./inputs.py)**: Como interagir com o usuário solicitando dados no console.

### Estruturas de Controle e Iteração

*   **[idade.py](./idade.py)**: Aplicação prática de condicionais (`if`, `else`, `elif`) para validação de faixas etárias.
*   **[contador.py](./contador.py)**: Demonstração básica de laços de repetição.
*   **[range.py](./range.py)**: Uso da função integrada `range()` para gerar sequências numéricas.
*   **[menu.py](./menu.py)**: Criação de um menu iterativo com loop `while` e interrupção controlada (`break`).

### Estruturas de Dados

*   **[listas.py](./listas.py)**: Manipulação, indexação e iteração sobre listas de itens.
*   **[dic.py](./dic.py)**: Criação, alteração e iteração sobre estruturas de chave-valor (dicionários).

### Modularização e Orientação a Objetos (POO)

*   **[funcoes.py](./funcoes.py)**: Declaração de funções com passagem de argumentos, retorno de valores e uso de anotações de tipo (*type hints*).
*   **[banco.py](./banco.py)**: Implementação completa de conceitos de Orientação a Objetos (Classes, Construtor `__init__`, Métodos, Herança e Polimorfismo) através de uma simulação de contas bancárias (Corrente e Poupança).
*   **[poo_exemplos.py](./poo_exemplos.py)**: Exemplos avançados e detalhados de POO, abordando Encapsulamento (atributos privados, getters e setters com `@property`), Herança, Polimorfismo, Abstração (classes abstratas com o módulo `abc`) e Métodos Mágicos (*dunder methods* como `__str__`, `__len__`, `__eq__`).

---

## 📝 Exercícios Práticos

O repositório também inclui desafios e exercícios práticos resolvidos:

*   **[ex1.py](./ex1.py)**: Formulário básico de cadastro recebendo dados via `input`.
*   **[ex5.py](./ex5.py)**: Evolução do cadastro salvando as informações dentro de um dicionário (`dict`) e formatando a saída de forma estruturada.
*   **[ex6.py](./ex6.py)**: Um mini-sistema de logística que calcula o valor total de uma entrega com base no valor do produto e no peso (calculando o frete via função dedicada).

---

## 🚀 Como Executar

### Pré-requisitos
Certifique-se de possuir o **Python 3** instalado em sua máquina. Para verificar, execute:
```bash
python --version
```

### Executando um Script
Para executar qualquer um dos scripts, abra o terminal na pasta raiz do projeto e execute o comando:
```bash
python <nome_do_arquivo>.py
```
Exemplo:
```bash
python banco.py
```
