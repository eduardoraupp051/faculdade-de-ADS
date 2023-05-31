let nome = prompt('Digite seu nome:');
let idade = prompt('Digite sua idade:');

if (idade >= 18) {
  alert(`${nome}, você tem ${idade} anos, portanto é maior de idade.`);
} else {
  alert(`${nome}, você tem ${idade} anos, portanto não é maior de idade.`);
}
