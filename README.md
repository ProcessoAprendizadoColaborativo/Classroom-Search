# Classroom Search

## Escopo do projeto

 Algoritmo para Localizar Sala de Aula

---

## Identificação do problema

O ensalamento na faculdade nem sempre é exato, e muitas das vezes gera retrabalho na secretaria para atualizar o ensalamento. Vários alunos sofrem para encontrar a sala exata do dia, caso houver uma troca.

---

## Objetivo

Desenvolver um algoritmo que possa resolver o ensalamento de forma prática, que gere resultados afim de ajudar a secretaria e alunos.
Terá uma tela mostrando a Sala/Laboratório, turma e quantidade de lugares. Sempre que for realizada a pesquisa do ensalamento ideal, o algoritmo realiza a busca das salas cruzando os dados de quantidades de alunos por turma com a quantidade de lugares de uma sala/laboratório. Quandou houver uma atualização na troca de salas, o algoritmo reconhece a troca e de imediato informa a sala ideal.


---

## Funcionalidades

- Cadastro de turmas e salas de aula: algoritmo busca no ensalamento;
- Cadastro de alunos: o sistema deve buscar banco de dados da católica;
- Busca de sala: o sistema deve permitir a busca de sala por nome do aluno ou professor;
- Conforme as especificações dos laboratórios ou salas de aula referentes a quantidade de computadores ou quantidade de carteiras disponíveis. a secretária irá colocar os professores e a quantidade de alunos de cada turma e o software vai definir ou melhor ensalamento.
- Apenas número de alunos por turma, e número disponível de computadores e/ou carteiras disponíveis por sala.
    
  |Entradas | Saidas |
  |---|---|
  | n_alunos_turma | cod_sala  |
  | n_pc-lab_sala  | cod_turma |
  | n_lugares_sala | cap_sala  |
  |                | qtd_sala |

## Artefatos

- Diagrama de classes;
- UML;
- Requisitos;

## Tecnologias

Linguagem de programação: o algoritmo será desenvolvido utilizando Python. 

Banco de dados: O banco de dados utilizado será o MySQL.

## Cronograma

Levantamento de requisitos: 1 semanas 

Desenvolvimento do banco de dados: 1 semanas 

Desenvolvimento do back-end: 4 semanas 

Desenvolvimento do front-end: 4 semanas 

Testes e correções: 2 semanas 

Implantação e treinamento: 1 semana 

## Equipe

- Desenvolvedores (2): Eder Ramos Filho e  Eduardo Paterno.

- Gerente de projeto (2): Khatlyllen Vyctória Constantino e Ruan Hoffmann Martins.


## Considerações Finais

0 == sala;
1 == turma;

O sistema deverá ser desenvolvido em conformidade com as normas de segurança e privacidade de dados.
O sistema deverá ser intuitivo e de fácil utilização.
O sistema deverá ser responsivo, adaptando-se a diferentes dispositivos (desktops, tablets e smartphones).
O sistema deverá ser testado antes da implantação.
Será realizado um treinamento para os usuários finais, a fim de garantir que saibam utilizar todas as funcionalidades do sistema.

## Contribuições

- Dê um Fork no Repositório
- Crie um branch: ```git checkout -b <nome_branch>.```
- Faça suas alterações e confirme-as: ```git commit -m '<mensagem_commit>'```
- Envie para o branch original: ```git push origin master```
- Crie a solicitação de pull
