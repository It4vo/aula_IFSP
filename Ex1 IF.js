
let idade = 17;
''
if (idade < 16) {
    console.log("Você é não-eleitor, pois tem menos de 16 anos.");
} else {
    if (idade >= 18 && idade <= 65) {
        console.log("Você é um eleitor obrigatório, pois tem entre 18 e 65 anos.");
    } else {
        if (idade >= 16 && idade < 18) {
            console.log("Você é um eleitor facultativo, pois tem entre 16 e 18 anos.");
        } else {
            console.log("Você é um eleitor facultativo, pois tem mais de 65 anos.");
        }
    }
}
