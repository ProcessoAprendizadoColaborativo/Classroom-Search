// Fazer a requisição para a API usando JavaScript

/*fetch('http://localhost:5000/api/dados')  // Substitua a URL pelo endpoint correto da sua API
  .then(response => response.json())
  .then(data => {
    // Manipular os dados recebidos
    const dadosApiElement = document.getElementById('dados-api');
    dadosApiElement.innerHTML = JSON.stringify(data);
  })
  .catch(error => {
    console.error('Erro na requisição:', error);
  });*/

  fetch('http://localhost:5500/salas')
  .then(response => response.json())
  .then(data => {
    // Manipular os dados recebidos
    const salasList = document.getElementById('salas-list');
    salasList.innerHTML = '';
    data.forEach(sala => {
      const salaItem = document.createElement('li');
      salaItem.innerText = `ID: ${sala.id_sala}, Ambiente: ${sala.Ambiente}, Posição: ${sala.Posicao}`;
      salasList.appendChild(salaItem);
    });
  })
  .catch(error => {
    console.error('Erro na requisição:', error);
  });

fetch('http://localhost:5500/turmas')
  .then(response => response.json())
  .then(data => {
    // Manipular os dados recebidos
    const turmasList = document.getElementById('turmas-list');
    turmasList.innerHTML = '';
    data.forEach(turma => {
      const turmaItem = document.createElement('li');
      turmaItem.innerText = `ID: ${turma.id_turma}, Qtd Alunos: ${turma.qtd_alunos}, Turno: ${turma.turno}`;
      turmasList.appendChild(turmaItem);
    });
  })
  .catch(error => {
    console.error('Erro na requisição:', error);
  });

