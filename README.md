<div align="center">
<img src="https://hermes.digitalinnovation.one/assets/diome/logo-full.svg" alt="Logo Bootcamp" width="80">
<h1>DIO BOOTCAMP</h1>
<img src="https://hermes.dio.me/tracks/f5dba255-da18-427a-a02a-ca11a339c1cd.png" alt="Logo Bootcamp" width="220">
</div>

#  :bank: Desafio: Otimizando o Sistema Bancário com Funções Python


## :memo: Objetivo Geral
Separar as funcões existentes de saque, depósito e extrato em
funcões. Criar duas novas funcées: cadastrar usuario (cliente) e cadastrar conta bancária.

## :battery: Stack utilizada
[![My Stack](https://skillicons.dev/icons?i=vscode,py,git)](https://skillicons.dev)

## :punch: Desafio
Precisamos deixar nosso código mais modularizado, para issovamos criar funções para as operações existentes: sacar,
depositar e visualizar histórico. Além disso, para a versão 2 do nosso sistema precisamos criar duas novas funções: criar
usuario (cliente do banco) e criar conta corrente (vincular com usuário).

## :knife: Separação em funções
Devemos criar funções para todas as operações do sistema. Para exercitar tudo o que aprendemos neste módulo, cada
função vai ter uma regra na passagem de argumentos. O retorno e a forma como serão chamadas, pode ser definida por
você da forma que achar melhor.

## :heavy_minus_sign: Saque
A função saque deve receber os argumentos apenas por nome (keyword only). Sugestão de argumentos: saldo, valor, extrato,
limite, numero_saques, limite_saques. Sugestão de retorno: saldo e extrato.

## :heavy_plus_sign: Depósito
A função depósito deve receber os argumentos apenas por posição (positional only). Sugestão de argumentos: saldo, valor, extrato. Sugestão de retorno: saldo e extrato.

## :tomato:	Extrato
A função extrato deve receber os argumentos por posição e nome (positional only e keyword only). Argumentos posicionais: saldo, argumentos nomeados: extrato.

## :new: Novas funções
Precisamos criar duas novas funções: criar usuário e criar conta corrente. Fique a vontade para criar mais funções, exemplo: listar contas.

## :bust_in_silhouette: Criar usuário (cliente)
O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e
endereço. O endereço é uma string com o formato: logradouro, nro - bairro - cidade/sigla estado. Deve ser armazenado
somente os números do CPF. Não podemos cadastrar 2 usuários com o mesmo CPF.

## :link: Criar conta corrente
O programa deve armazenar contas em uma lista, uma conta é composta por: agência, número da conta e usuário. O número
da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001". O usuário pode ter mais de uma conta, mas uma
conta pertence a somente um usuário.

<br>

> [!NOTE]
> Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF informado para cada usuário da lista.

<br>

## :bank: Link do primeiro desafio: [Criando um sistema bancário](https://github.com/walterowisk/DIO_LabProject-SistemaBancarioComPython)