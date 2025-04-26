async function classificarTexto() {
    const texto = document.getElementById('texto').value;
  
    const resposta = await fetch('/classificar', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ texto })
    });
  
    const resultado = await resposta.json();
    document.getElementById('resultado').textContent = resultado.classificacao;
  }