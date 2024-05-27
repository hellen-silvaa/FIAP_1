var resultado = document.getElementById('resultado')

function calcular() {
    var numBooks = parseInt(document.getElementById("numBooks").value);
    var preco = ""

    if (numBooks >= 7) {
        preco = 15 * 7;
    }

    if (numBooks <= 0) {
        preco = 'Valor inválido'

    } else {
        preco = 22 * 7;
    }

    resultado.innerText = `O preço total é ${preco}`

}