function contar() {
    var num1 = parseInt(document.getElementById("num1").value);
    console.log(`Os números divisiveis por ${num1}  é:`)
    for (i = 1; i <= num1; i++) {
        if (num1 % i === 0) {
            console.log(i)
        }
    }
}