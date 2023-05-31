let numero = prompt('Digite um número:')
let texto = 'O número '

if (numero % 2 == 0){
    texto = `${texto} ${numero} é par  `
}else{
    texto - `${texto} ${numero} é impar `
}
if(numero >=0){
    texto = `${texto} e positivo.`
}else{
    texto = `${texto} e negativo`
}
alert(texto);
