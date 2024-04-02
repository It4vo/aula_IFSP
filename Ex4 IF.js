// Leitura das notas e quantidade de faltas
let prova1 = 10
let prova2 = 5
let tr = 3
let faltas = 14


let media = ((prova1 * 0.4) + (prova2 * 0.6)) * 0.7 + tr;

let situacao;
if (faltas >= 24) {
    situacao = "Reprovado por faltas";
} else {
    if (media >= 6) {
        situacao = "Aprovado";
    } else{ if (media >= 3) {
        situacao = "Em exame";

    } else {
        situacao = "Reprovado";
    }
}
}


console.log("Situação do aluno:", situacao);
console.log("Média:", media);
