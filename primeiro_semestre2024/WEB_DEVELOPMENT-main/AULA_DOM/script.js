const btnCriar = document.querySelector('#btnCriar');
const inputUsuario = document.querySelector('#inputUsuario');
const listaFilmes = document.querySelector('#listaFilmes');


const filmes = [
    {
        nome: "Como se eu fosse você",
        diretor: 'Tony Ramos',
        ano: 2004,
        sinopse: "Se Eu Fosse Você é um filme brasileiro de 2006, do gênero comédia romântica, dirigido por Daniel Filho e estrelado por Glória Pires e Tony Ramos."
    },
    {
        nome: "Forrest Gump",
        diretor: "Robert Zemeckis",
        ano: 1994,
        sinopse: "bla"

    },
    {
        nome: "Operação Big Hero",
        diretor: "Tony Hawk",
        ano: 2014,
        sinopse: "blabla"
    }
]

btnCriar.addEventListener('click', function (infosDoEvento){
    infosDoEvento.preventDefault();

        let novoFilme = document.createElement('li');
        novoFilme.innerText = inputUsuario.value;

        let btnEditar = document.createElement('button')
        btnEditar.innerText = "Editar"
        btnEditar.addEventListener('click', function(){
                novoFilme.style.backgroundColor = "black"    
                novoFilme.classList.toggle('mudar-cor')           
        })

        let imagemFilme = document.createElement('img')
        imagemFilme.src = ""
        imagemFilme.alt = ""
        novoFilme.append(btnEditar)

        novoFilme.innerHTML = `
        <h1> Titulo do filme</h1>
        <p> Sinopse</p>
        <p> Avaliação</p>  `

        listaFilmes.append(novoFilme);

        inputUsuario.value = " "
})

//infosDoEvento = parâmetro que guarda todas as informações do clique
//infosDoEvento.target = elemento que disparou o evento
//infosDoEvento.target.id = id do elemento que foi clicado
//infosDoEvento.parentNode = PEGA O ELEMENTO PAI DO ELEMENTO que foi clicado
//.createElement - cria um novo elemento html
//.append - adiciona um elemento dentro de outro elemento html 

//CREATE 
function criarFilme(){
    let filmeAdicionado = {
        nome: inputUsuario.value,
        diretor: inputDiretor.value,
        ano: inputAno.value,
        sinopse: inputSinopse.value
    }
}
    filmes.unshift(filmeAdicionado)
    renderizarNaTela()

//READ
window.onload = renderizarNaTela()
function renderizarNaTela(){
    
    filmes.forEach(
        filme => {
            let novoFilme = document.createElement('li');
            novoFilme.innerHTML = `
            <h1> ${filme.nome}</h1>
            <img src = ${filme.imagem}/>
            <p>${filme.diretor}</p>
            <p>${filme.sinopse}</p>
            `

            listaFilmes.append(novoFilme)
        }
    )
}

//UPDATE


//DELETE