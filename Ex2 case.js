
console.log("============= MENU =============");
console.log("a = saldo");
console.log("b = depósito");
console.log("c = pagamentos");
console.log("d = transferências");
console.log("e = sair");
console.log("=================================");


opcao="a"


switch (opcao) {
    case 'a':
        console.log("Opção selecionada: saldo");
        
        break;
    case 'b':
        console.log("Opção selecionada: depósito");
        
        break;
    case 'c':
        console.log("Opção selecionada: pagamentos");
        
        break;
    case 'd':
        console.log("Opção selecionada: transferências");
       
        break;
    case 'e':
        console.log("Opção selecionada: sair");
        
        break;
    default:
        console.log("Opção inválida.");
      
}
