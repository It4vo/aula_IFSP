
let salario = 750; 



if (salario < 500) {
    salarioReajustado = salario * 1.15; 
} else if (salario >= 500 && salario <= 1000) {
    salarioReajustado = salario * 1.10; 
} else {
    salarioReajustado = salario * 1.05;
}


salarioReajustado = salarioReajustado;


console.log("Salário antigo: R$" + salario);
console.log("Salário reajustado: R$" + salarioReajustado);
