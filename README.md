![Design sem nome (11)-fococlipping-standard](https://github.com/ProcessoAprendizadoColaborativo/Classroom-Search/assets/29105030/54cef8fc-702e-4e78-aeff-8b40389527e4)

## Equipe

- Desenvolvedores: Eder Ramos Filho e  Eduardo Paterno.

- Gerente de projeto: Khatlyllen Vyctória Constantino e Ruan Hoffmann Martins.

## Identificação do problema

O problema encontrado foi que o ensalamento na faculdade nem sempre é exato, e muitas das vezes gera retrabalho na secretaria para atualizar o ensalamento. Todo processo é feito manualmente. Portanto decidimos automatizar o ensalamento utilizando 

## Requisitos funcionais

- Permitir cadastrar turmas. o algoritmo deve cadastrar as turmas com:
  - Código da turma;
  - nº de alunos;
  - tipo de sala.
- Também buscar os respectivos dados no banco de dados criado;

- Permitir cadastrar salas/Laboratórios.
  - Código de ambiente;
  - tipo de sala;
  - nº de lugares.
  
- Permitir atualizar o ensalamento. 

- O sistema deve apresentar a sala de aula com o código da turma e o nº de lugares. 

## Requisitos não funcionais

- Desempenho: o sistema deve ser prático e de rápida resposta a solicitação.

- Confiabilidade: o sistema deve ser confiável e ser acertivo da distribuição das salas/lab em até 95%.

- Interface: o sistema deve apresentar uma interface amigável e intuitiva, para facilitar a navegação do usuário e tornar a experiência de uso agradável.

## Restrições

- O acesso aos dados por parte da Católica foi dificultado, então decidimos fazer com que a secretária digitasse os dados pela primeira vez.
- O algoritmo foi uma das restrições, pois o modelo de IA que usamos na maioria do projeto no fim não estava sendo acertiva.
- API.

## UML

![UML PAC 7 drawio](https://user-images.githubusercontent.com/29105030/236072075-78744beb-7757-42df-98d1-303dbfcb678d.png)

## Tecnologias utilizadas

### Banco de dados

O banco de dados utilizado será o MySQL.

![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white).

![WhatsApp Image 2023-05-10 at 20 49 54](https://github.com/ProcessoAprendizadoColaborativo/Classroom-Search/assets/29105030/f4a26d54-d7de-40dc-864a-88bda29d4fda)
______________________

## Back-end

- O calculo combinatório direto no terminal.

![WhatsApp Image 2023-07-05 at 19 35 01](https://github.com/ProcessoAprendizadoColaborativo/Classroom-Search/assets/29105030/a024445a-1531-4c68-8f3e-6205a69270fc)



### ALGORITMO 
Será desenvolvido utilizando ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

É  um algoritmo de análise combinatória, que pega a quantidade de lugares das salas, quantidade de alunos por turmas, as restrições de dia da semana ou se a sala é laboratório ou não.


## Front-end

![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)

### Tela de Cadastro de sala.

![WhatsApp Image 2023-07-05 at 19 23 14](https://github.com/ProcessoAprendizadoColaborativo/Classroom-Search/assets/29105030/954e9b89-6856-4e51-8a68-0ccf8a516e08)

### Salas cadastradas

![WhatsApp Image 2023-07-05 at 19 23 50](https://github.com/ProcessoAprendizadoColaborativo/Classroom-Search/assets/29105030/245d307d-91a7-472d-ad6b-0f069cf291da)

### Cadastro de turma

![WhatsApp Image 2023-07-05 at 19 24 12](https://github.com/ProcessoAprendizadoColaborativo/Classroom-Search/assets/29105030/0e601008-a909-4b1d-b09b-b91fb61b42f3)

### Turmas cadastradas

![WhatsApp Image 2023-07-05 at 19 25 06 (1)](https://github.com/ProcessoAprendizadoColaborativo/Classroom-Search/assets/29105030/70259d88-fb5c-4bd0-a952-281e23edc8e6)

### Calcular o ensalamento

![WhatsApp Image 2023-07-05 at 19 25 06 (2)](https://github.com/ProcessoAprendizadoColaborativo/Classroom-Search/assets/29105030/34d9813a-1d82-4643-bb93-a29075eeaeae)


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
