let nota1 = parseFloat(prompt('digite a primeira nota'))
let nota2 = parseFloat(prompt('digite a segunda nota'))
let nota3 = parseFloat(prompt('digite a terceira nota'))

let soma = nota1 + nota2 + nota3

media = soma / 3

if (media >= 6) {
    alert('voce passou');
}

else {
    alert('voce rodou')
}