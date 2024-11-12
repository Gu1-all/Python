const desconto = 0.1
const juros = 0.2

let produto = {
    nome: 'Teclado',
    codigo: '123456',
    valor: 270.50
}

let produto2 = {
    nome: 'Microfone',
    codigo: '654321',
    valor: 220.30
}

let produto3 = {
    nome: 'Livro',
    codigo: '231564',
    valor: 200
}

function calcularCompra (produto, numParcelas){
    let valor = produto.valor;
    let valorParcelado = produto.valor / numParcelas

    let valorDesconto = valor * desconto
    let valorDescontoCalc = valor - valorDesconto

    let valorJuros = valor * juros
    let valorJurosCalc = valor + valorJuros
    let valorParcelJuros = valorJurosCalc / numParcelas

    if (numParcelas == 0) {
        console.log(`Comprando a vista com 10% de desconto o valor final fica: R$ ${valorDescontoCalc.toFixed(2).replace('.' , ',')}`)
    }
    else if (numParcelas <= 10) { 
        console.log(`Comprando o ${produto.nome} em ${numParcelas} parcelas, você terá ${numParcelas} parcelas sem juros de ${valorParcelado.toFixed(2).replace(',' , ',')}`)
    }
    else if (numParcelas >= 11 || numParcelas <= 12) {
        console.log(`Comprando o ${produto.nome} em ${numParcelas} parcelas, vocẽ terá ${numParcelas} parcelas de ${valorParcelJuros.toFixed(2).replace('.' , ',')} com 2% de juros total.`)
    }
    else {
        console.log('Número de Parcelas invalido')
    }
}

calcularCompra(produto, 0) // Compra à vista, exibe o valor com desconto.
calcularCompra(produto2, 5) // Compra parcelada em 5x, exibe o valor de cada parcela.
calcularCompra(produto3, 11) // Compra parcelada em 11x, exibe o valor de cada parcela com juros.
