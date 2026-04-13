const form = document.getElementById("product-form");

form.addEventListener("submit", async (event) => {
    event.preventDefault();

    // Pegando valores dos inputs
    const tipoCliente = document.getElementById("tp_cliente").value;
    const valor = parseFloat(document.getElementById("valor").value);
    const desconto = parseFloat(document.getElementById("desconto").value) || 0;

    // Enviando para o backend
    const response = await fetch("http://localhost:5000/cashback", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            tp_cliente: tipoCliente,
            valor: valor,
            desconto: desconto
        })
    });

    const data = await response.json();

     const resultado = document.getElementById("resultado");

    resultado.innerHTML = `
        <div class="resultado-box">
            Valor final: R$ ${data.valor_final.toFixed(2)} <br>
            Cashback: R$ ${data.cashback.toFixed(2)}
        </div>
    `;
});