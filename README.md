![Design sem nome (11)-fococlipping-standard](https://github.com/ProcessoAprendizadoColaborativo/Classroom-Search/assets/29105030/54cef8fc-702e-4e78-aeff-8b40389527e4)

## Equipe

- Eder Ramos Filho.
- Eduardo Paterno.
- Khatlyllen Vyctória Constantino.
- Ruan Hoffmann Martins.

## Relevância

O problema encontrado foi que o ensalamento na faculdade nem sempre é exato e rápido, e muitas das vezes gera retrabalho na secretaria para atualizar o ensalamento. Todo processo é feito manualmente olhando uma lista em excel e comparando com outra lista, qual sala é mais ideal. Portanto decidimos automatizar o ensalamento utilizando um algoritmo de análise combinatória. Assim nosso objetivo é trazer a melhor proximidade de sala e turmas.

## Requisitos funcionais

- O algoritmo deve permitir cadastrar turmas com:
  - Código da turma;
  - nº de alunos;
  - tipo de sala.
  - Dia da semana;
  - Também buscar os respectivos dados no banco de dados criado;

- Permitir cadastrar salas/Laboratórios com:
  - Código de ambiente;
  - tipo de sala;
  - nº de lugares.
  
- Permitir gerar o ensalamento. 

- O sistema deve apresentar a sala de aula com o código da turma e o nº de lugares. 

## Requisitos não funcionais

- Desempenho: o sistema deve ser prático e de rápida resposta a solicitação.

- Interface: o sistema deve apresentar uma interface amigável e intuitiva, para facilitar a navegação do usuário e tornar a experiência de uso agradável.

## Restrições

- O acesso aos dados por parte da Católica foi dificultado, então decidimos fazer com que o usuário digitasse os dados pela primeira vez.
- O algoritmo foi uma das restrições, pois o modelo de IA que usamos na maioria do projeto no fim não estava sendo acertiva. Então decidimos alterar para um algoritmo de regressão linear.
- A API apresentou algumas dificuldades e nos deixou inseguros quanto ao seu uso, portanto decidimos usar apenas o terminal.
- AWS por ser greatuíto, acabou dando um custo inesperado na tentativa de subir para nuvem.

## UML

- A seguir o uml do projeto de como ele deve funcionar.

![UML PAC 7 drawio](https://user-images.githubusercontent.com/29105030/236072075-78744beb-7757-42df-98d1-303dbfcb678d.png)

## Tecnologias utilizadas

- Bootstrap.
- Mysql.
- Python.
- Xampp.

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

### Banco de dados

O banco de dados utilizado é MySQL.

![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white).

![WhatsApp Image 2023-05-10 at 20 49 54](https://github.com/ProcessoAprendizadoColaborativo/Classroom-Search/assets/29105030/f4a26d54-d7de-40dc-864a-88bda29d4fda)

## Tabela de salas

![image](https://github.com/ProcessoAprendizadoColaborativo/Classroom-Search/assets/29105030/3f687e45-4c39-40d3-9c78-fe44d626a483)


## Tabela turmas

![image](https://github.com/ProcessoAprendizadoColaborativo/Classroom-Search/assets/29105030/24fefc5f-d84f-459f-89bb-9af8f148c17e)


## Servidor: Xampp

- Para rodar a ligação de banco e algoritmo, deve inicializar o seu servidor Xampp, selecionando o Mysql.

![image](https://github.com/ProcessoAprendizadoColaborativo/Classroom-Search/assets/29105030/a16fb118-a63d-4bde-8473-826f55f28757)

## Back-end 

Desenvolvido utilizando ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

### Algoritmo

É um algoritmo de análise combinatória por Regressão Linear. Ele é utilizado para treinar um modelo que prevê a quantidade de alunos de uma turma com base na quantidade de lugares disponíveis nas salas. O modelo é treinado usando os dados das salas e turmas inseridos no banco de dados e, em seguida, são encontradas as combinações válidas de salas e turmas que atendem a duas determinadas restrições de dia da semana ou se a sala é laboratório ou não. A diferença máxima entre a quantidade de lugares disponíveis e a quantidade de alunos.
  
### Registro de dados de salas e turmas

-Inserindo os dados:

![image](https://github.com/ProcessoAprendizadoColaborativo/Classroom-Search/assets/29105030/20dc6e81-6234-4f5e-b62c-9cddce24abf2)

- Combinação de salas e turmas:

![image](https://github.com/ProcessoAprendizadoColaborativo/Classroom-Search/assets/29105030/27fc1d00-0e6a-4b2b-b601-cb73e163201a)


## Considerações Finais

O trabalho no geral foi um desafio bem interessante, que nos exigiu muito a capacidade de analisar o problema por diversas óticas. Pensamos em algumas possíveis soluções porém nenhuma chegava perto do resultado esperado. O que nos fortaleceu como equipe foi saber dos limites de cada um e buscar aprender novas habilidades para ajudar o grupo.
Sabemos que o resultado obtido poderia ter sido mais satisfatório, porém o avanço que demos em aplicar novos conhecimentos ao projeto já nos deixa satisfeitos. Agradecemos também ao professor Camargo por nos ajudar e dar ideias para soluções.


