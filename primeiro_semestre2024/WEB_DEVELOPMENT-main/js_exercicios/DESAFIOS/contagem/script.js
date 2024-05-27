//exemplo
// var i = 0
// while (i<10) {
//     console.log(i)
//     i++
// }

// desafio contagem regressiva
function contar() {
    var num1 = parseInt(document.getElementById("num1").value);
    while (num1 > 0) {
        console.log(num1)
        num1--
    }
}

for(i=0; i<=10;i++){
    console.log(i)
}

// i=0 | i é menor que 10? | printa na tela o 0
// i=1 | i é menor que 10? | printa na tela o 1
// ...
// i=11 | i é menor que 10? | sai do loop
// +=2 'soma de dois em dois'
//i-- diminui