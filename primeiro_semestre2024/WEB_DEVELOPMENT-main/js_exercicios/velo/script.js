var resultado = document.getElementById('resultado')

function velocidade() {
    var numVelo = parseInt(document.getElementById("numVelo").value);
    var multa = ""

    if (numVelo >= 60) {
        multa = (numVelo - 60) * 100;
    }

    else if (numVelo <= 0) {
        multa = 'Valor inválido'

    } else {
        multa = 'Esta andando corretamente, parabéns!!!!';
    }

    resultado.innerText = `O valor da sua multa é: ${multa}`

}

// default = else