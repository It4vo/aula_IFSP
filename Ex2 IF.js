
let A = 7;
let B = 3;
let C = 10;


if (A > B) {
    let vazio = A;
    A = B;
    B = vazio;
}

if (B > C) {
    let vazio = B;
    B = C;
    C = vazio;
}

if (A > B) {
    let vazio = A;
    A = B;
    B = vazio;
}

console.log("Os valores em ordem crescente são:", A, B, C);
