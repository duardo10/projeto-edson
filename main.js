function createClient() {
    const clientName = document.getElementById("client-name").value;
    const clientCity = document.getElementById("client-city").value;
    const debtStartDate = document.getElementById("debt-start-date").value;
    const debtEndDate = document.getElementById("debt-end-date").value;

    // Envia os dados para o backend usando a API fetch ou outra biblioteca
    fetch('/api/clientes/create', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `name=${encodeURIComponent(clientName)}&city=${encodeURIComponent(clientCity)}&debt-start=${encodeURIComponent(debtStartDate)}&debt-end=${encodeURIComponent(debtEndDate)}`
    })
    .then(response => response.json())
    .then(data => {
        // Atualiza a lista de clientes com o novo cliente
        populateClientList();
        // Limpa os campos do formulário
        document.getElementById("client-name").value = "";
        document.getElementById("client-city").value = "";
        document.getElementById("debt-start-date").value = "";
        document.getElementById("debt-end-date").value = "";
    })
    .catch(error => {
        console.error('Erro ao adicionar cliente:', error);
    });
}