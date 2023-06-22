// Fazer a requisição para a API usando JavaScript

fetch('http://localhost:5000/api/dados')  // Substitua a URL pelo endpoint correto da sua API
  .then(response => response.json())
  .then(data => {
    // Manipular os dados recebidos
    const dadosApiElement = document.getElementById('dados-api');
    dadosApiElement.innerHTML = JSON.stringify(data);
  })
  .catch(error => {
    console.error('Erro na requisição:', error);
  });
