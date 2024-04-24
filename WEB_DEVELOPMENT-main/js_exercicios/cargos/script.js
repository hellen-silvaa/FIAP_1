function calcular() {
    cargo = document.getElementById('numCargo').value
    var resultado = document.getElementById('resultado')
    inicio = 3000
    switch (cargo) {
        case 'Jr':
            resultado.innerText = `'O seu sálario é ${inicio} '`
            break;
        case 'Pleno':
            console.log(`'O seu sálario é ${inicio * 2}'`)
            break;
        case 'Sênior':
            console.log(`'O seu sálario é ${inicio * 2}'`)
            break;
        case 'Tech Lead':
            console.log(`'O seu sálario é ${inicio * 2}'`)
            break;
        case 'Diretor':
            console.log(`'O seu sálario é ${inicio * 2}'`)
            break;
        default:
            console.log(`'Você é desempregado'`)
            break;
    }
}