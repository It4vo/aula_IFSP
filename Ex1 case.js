// Dados de entrada
var altura = 1.75;  // Altura em metros
var sexo = 'M';     // 'M' para masculino, 'F' para feminino

// Determinar o peso ideal de acordo com o sexo
var peso_ideal;
if (sexo == 'M') {
    peso_ideal = 72.7 * altura - 58;
} else {
    if (sexo == 'F') {
    peso_ideal = 62.1 * altura - 44.7;
} else {
    console.log("Por favor, insira 'M' para masculino ou 'F' para feminino.");
}
}

console.log("O peso ideal é:", peso_ideal, "kg");
