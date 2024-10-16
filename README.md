# Sistema Bancário em POO

Esse projeto foi desenvolvido como parte de um desafio acadêmico, onde o objetivo era modelar um sistema bancário utilizando Programação Orientada a Objetos (POO). O sistema permite que usuários realizem operações bancárias como depósitos, saques e gerenciamento de contas.

## Desafio 1 - Modelagem do Sistema Bancário

### O que foi feito:
1. **Criação de Classes:**
   - **Cliente:** Representa os clientes do banco, com a capacidade de adicionar contas e realizar transações.
   - **Pessoa Física:** Uma subclass de `Cliente`, que armazena informações específicas como nome, CPF e data de nascimento.
   - **Conta:** Classe base para contas bancárias, com métodos para sacar e depositar.
   - **Conta Corrente:** Herda de `Conta` e possui limites específicos para saques.
   - **Transações:** Classes para `Saque` e `Deposito`, que implementam um sistema de registro de transações.

2. **Histórico de Transações:**
   - Implementamos uma classe `Historico` que armazena o histórico de transações de cada conta.

3. **Controle de Saldo e Limites:**
   - O sistema verifica se as operações são válidas, como saldo suficiente para saques e limites de transações.

## Desafio Extra - Atualizando o Menu

### O que foi feito:
1. **Interface de Usuário:**
   - Criamos um menu interativo que permite ao usuário escolher entre várias operações bancárias, como:
     - Depositar
     - Sacar
     - Criar Usuário
     - Criar Conta Corrente
     - Listar Contas
     - Sair

2. **Funções de Ação:**
   - As operações de depósito e saque agora interagem diretamente com as classes criadas, utilizando os métodos apropriados.
   - Implementamos funções para criar usuários e contas, listando as contas cadastradas e validando entradas de CPF.

### Resumo das Melhorias

- **Estrutura Orientada a Objetos:** O sistema foi desenvolvido usando POO, com classes que representam as principais entidades do sistema bancário.
- **Separação de Responsabilidades:** Cada classe tem uma função clara, facilitando a manutenção e a escalabilidade.
- **Interação do Usuário:** Um menu foi implementado para que os usuários possam interagir com o sistema de maneira intuitiva.
- **Tratamento de Erros:** O código agora lida com erros comuns, como saldo insuficiente ou CPF já cadastrado.

## Como Executar

Para rodar o sistema, basta executar o arquivo Python no seu ambiente local. Certifique-se de ter o Python instalado.

```bash
python nome_do_arquivo.py
