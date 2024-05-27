// desafio tabuada com for

// for(i=10; i>=0; i--){
//     console.log(i)
// }


function tabuada() {
    var tab = parseInt(document.getElementById("tab").value);
    for(i=1; i<=10;i++){
        console.log(`A tabuada do número ${tab} X ${i} é ${tab * i}`)

    }

}

