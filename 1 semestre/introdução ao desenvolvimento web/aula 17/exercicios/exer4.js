let numero = prompt('Digite um número:');
numero = Number(numero);

for (let i = 1; i <= 10; i++) {
  let resultado = numero * i;
  alert(`${numero} x ${i} = ${resultado}`);
}
