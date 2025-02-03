document.getElementById('cadastroForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const nome = document.getElementById('nome').value;
    const descricao = document.getElementById('descricao').value;

    const response = await fetch('http://localhost:8000/items/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name: nome, description: descricao }),
    });

    if (response.ok) {
        alert('Equipamento cadastrado com sucesso!');
    } else {
        alert('Erro ao cadastrar equipamento');
    }
});

document.getElementById('registroForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const equipamentoId = document.getElementById('equipamentoId').value;
    const atividade = document.getElementById('atividade').value;

    const response = await fetch('http://localhost:8000/atividades', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ equipamentoId, atividade }),
    });

    if (response.ok) {
        alert('Atividade registrada com sucesso!');
    } else {
        alert('Erro ao registrar atividade');
    }
});

document.getElementById('deviceForm').addEventListener('submit', (e) => {
    e.preventDefault();
    const deviceType = document.getElementById('deviceType').value;
    window.location.href = `cadpc.html?deviceType=${deviceType}`;
});

async function carregarEquipamentos() {
    const response = await fetch('http://localhost:8000/items/');
    const equipamentos = await response.json();

    const tabela = document.getElementById('equipamentosTable');
    // Atualizar a tabela com os dados recebidos
}
