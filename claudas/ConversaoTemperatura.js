function calcular() {
    const numero = parseInt(document.getElementById("numero").value);
    const respostaDiv = document.getElementById("resposta");

    if (document.getElementById("tempCelsiusFahrenheit").checked) {
        const resultado = CelsiusParaFahrenheit(numero);
        respostaDiv.textContent = `Resultado: ${numero}°C = ${resultado.toFixed(2)}°F`;
    } else if (document.getElementById("tempFahrenheitCelsius").checked) {
        const resultado = FahrenheitParaCelsius(numero);
        respostaDiv.textContent = `Resultado: ${numero}°F = ${resultado.toFixed(2)}°C`;
    }
}

function CelsiusParaFahrenheit(num) {
    return 1.8 * num + 32;
}

function FahrenheitParaCelsius(num) {
    return (num - 32) * 5 / 9;
}

function limparCampos() {
    document.getElementById("numero").value = '';
    document.getElementById("resposta").textContent = '';
    console.log("Limpar Campos");
}
