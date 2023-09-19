function createClient() {
    const clientName = document.getElementById("client-name").value;
    const clientStreet = document.getElementById("client-street").value;
    const clientNumber = document.getElementById("client-number").value;
    const clientCity = document.getElementById("client-city").value;
    const clientState = document.getElementById("client-state").value;
    const clientZip = document.getElementById("client-zip").value;
    const debtStartDate = document.getElementById("debt-start-date").value;
    const debtEndDate = document.getElementById("debt-end-date").value;

    // Envia os dados para o backend usando a API fetch ou outra biblioteca
    fetch('/api/clientes', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            nome: clientName,
            rua: clientStreet,
            numero: clientNumber,
            cidade: clientCity,
            estado: clientState,
            cep: clientZip,
            data_inicio_divida: debtStartDate,
            data_fim_divida: debtEndDate
        })
    })
    .then(response => response.json())
    .then(data => {
        // Atualiza a lista de clientes com o novo cliente
        populateClientList();
        // Limpa os campos do formulário
        document.getElementById("client-name").value = "";
        document.getElementById("client-street").value = "";
        document.getElementById("client-number").value = "";
        document.getElementById("client-city").value = "";
        document.getElementById("client-state").value = "";
        document.getElementById("client-zip").value = "";
        document.getElementById("debt-start-date").value = "";
        document.getElementById("debt-end-date").value = "";
    })
    .catch(error => {
        console.error('Erro ao adicionar cliente:', error);
    });
}
