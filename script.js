async function fetchData() {
  try {
    const responseSalas = await fetch('http://localhost:3000/salas');
    const salasData = await responseSalas.json();
    
    const salasList = document.getElementById('salas-list');
    salasList.innerHTML = '';
    salasData.forEach(sala => {
      const salaItem = document.createElement('li');
      salaItem.innerText = `ID: ${sala.id_sala}, Ambiente: ${sala.Ambiente}, Posição: ${sala.Posicao}`;
      salasList.appendChild(salaItem);
    });

    const responseTurmas = await fetch('http://localhost:3000/turmas');
    const turmasData = await responseTurmas.json();
    
    const turmasList = document.getElementById('turmas-list');
    turmasList.innerHTML = '';
    turmasData.forEach(turma => {
      const turmaItem = document.createElement('li');
      turmaItem.innerText = `ID: ${turma.id_turma}, Qtd Alunos: ${turma.qtd_alunos}, Turno: ${turma.turno}`;
      turmasList.appendChild(turmaItem);
    });
  } catch (error) {
    console.error('Erro na requisição:', error);
  }
}

// Chame a função fetchData apenas se estiver executando em um ambiente JavaScript real, como um navegador web.
if (typeof window !== 'undefined') {
  fetchData();
}
