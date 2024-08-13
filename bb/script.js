// item 1
console.log("Script Carregar");

//item 2
function calcularAnos() {

    //item 3
    console.log("Botão de calcular clicando");

    //item 4
    let popAinput = document.getElementById("popA").value.trim();

    //item 5
    let taxaAinput = document.getElementById("taxaA").value.trim();

    //item 6
    let popBinput = document.getElementById("popB").value.trim();

    //item 7
    let taxaBinput = document.getElementById("taxaB").value.trim();

    //item 8
    if (popAinput === "" || taxaAinput === "" || popBinput === "" || taxaBinput === ""){

        //item 9
        alert("Por favor preencha todos os campos");

        //item 10
        return;
        //item 11
    }
    //item 12
    let popA = parseInt(popAinput);

    //item 13
    let taxaA = parseFloat(taxaAinput) / 100;

    //item 14
    let popB = parseInt(popBinput);

    //item 15
    let taxaB = parseFloat(popBinput) / 100;

    //item 16
    let anos = 0;

    //item 17
    while (popA < popB) {

        //item 18
        popA *= (1 + taxaA);
        popB *= (1 + taxaB);
        anos++;
    }

    //item 20
    console.log("Anos calculados", anos);

    //item 21
    let resultado = document.getElementById ("resultado");

    resultado.innerHTML=`Serão necessários $(anos) anos para que a população do país A ultrapasse ou iguale a população do país B`

}
function limparCampos(){










}