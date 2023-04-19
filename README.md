# Classroom Search

## Identificação do problema

O problema encontrado foi que o ensalamento na faculdade nem sempre é exato, e muitas das vezes gera retrabalho na secretaria para atualizar o ensalamento. Vários alunos sofrem para encontrar a sala exata do dia, caso houver uma troca o que gera transtorno ter que ir de bloco em bloco procurar.


## Objetivo

Nosso objetivo para resolver esse problema, é desenvolver um algoritmo que possa ajustar o ensalamento de forma prática, que gere resultados afim de ajudar a secretaria e alunos.
Terá uma tela mostrando a Sala/Laboratório, turma e quantidade de lugares. Sempre que for realizada a pesquisa do ensalamento ideal, o algoritmo realiza a busca das salas cruzando os dados de quantidades de alunos por turma com a quantidade de lugares de uma sala/laboratório. Quando houver uma atualização na troca de salas, o algoritmo reconhece a troca e de imediato informa a sala ideal.


## Requisitos

Para efetivação deste projeto, o repositório possui endpoints que farão a manipulação do banco de dados com a regra de negócio do projeto, tendo as principais entidades do projeto como: Sala, Aluno, buscar e cadastrar. O projeto usa MySQL e Python. Para os principais pontos que o sistema deve atender, foram criados requisitos de sistemas, que são descrições das funcionalidades, sejam elas funcionais ou não funcionais.


## Requisitos funcionais

-O sistema deve permitir que o usuário insira o número da sala de aula que deseja localizar.
-O sistema deve apresentar a localização da sala de aula. 
-O sistema deve permitir que o usuário visualize informações adicionais sobre a sala de aula, como o nome do professor responsável.
-O sistema deve atualizar as informações de localização da sala de aula em tempo real, de forma que o usuário possa saber se a sala está ocupada ou livre.


## Requisitos não funcionais

-Desempenho: o sistema deve ser rápido e responsivo, para garantir que o usuário possa facilmente obter informações sobre a localização da sala de aula.
-Confiabilidade: o sistema deve ser confiável e estar disponível em até 95%.
-Escalabilidade: o sistema deve ser escalável para acomodar um grande número de usuários e salas de aula sem comprometer o desempenho.
-Interface amigável: o sistema deve apresentar uma interface amigável e intuitiva, para facilitar a navegação dos usuários e tornar a experiência de uso agradável.


## Funcionalidades

- Cadastro de turmas: algoritmo deve cadastrar as turmas com o nº de alunos. E também buscar os respectivos dados no banco de dados criado;
- Cadastro de sala/laboratório: o algoritmo deve cadastrar as salas/laboratórios com os nº de carteiras/PC disposíveis. E deve buscar banco de dados essas informações;
- Busca de sala: o sistema deve permitir a busca de sala por nome do aluno ou professor;
- Conforme as especificações dos laboratórios ou salas de aula referentes a quantidade de computadores ou quantidade de carteiras disponíveis. a secretária irá colocar os professores e a quantidade de alunos de cada turma e o software vai definir ou melhor ensalamento.
- Apenas número de alunos por turma, e número disponível de computadores e/ou carteiras disponíveis por sala.
    
  |Entradas | Saidas |
  |---|---|
  | n_alunos_turma | cod_sala  |
  | n_pc-lab_sala  | cod_turma |
  | n_lugares_sala | cap_sala  |
  |                | qtd_sala |


## Diagrama de classes

![Diagrama sem nome drawio (1)](https://user-images.githubusercontent.com/29105030/233210417-059fd366-1e1d-449e-960b-cfe7cfb0ad35.png)

## UML

![image](https://user-images.githubusercontent.com/29105030/233210823-fc442019-5080-4619-8d33-344c12e85ac0.png)


## Tecnologias

Linguagem de programação: o algoritmo será desenvolvido utilizando Python. 

Banco de dados: O banco de dados utilizado será o MySQL.

## Cronograma

Levantamento de requisitos: 1 semanas 

Desenvolvimento do banco de dados: 1 semana.

Desenvolvimento do back-end: 4 semanas 

Desenvolvimento do front-end: 2 semanas 

Testes e correções: 2 semanas 

Implantação e treinamento: 1 semana 

## Equipe

- Desenvolvedores (2): Eder Ramos Filho e  Eduardo Paterno.

- Gerente de projeto (2): Khatlyllen Vyctória Constantino e Ruan Hoffmann Martins.


## Considerações Finais

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
