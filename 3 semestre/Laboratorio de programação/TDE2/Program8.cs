// Escreva um programa que recebe via teclado dois números inteiros x e y e imprima no
// console se x é par ou não e se y é par ou não. Use o operador condicional ternário (? :)


//Solicita ao usuario que insira dois numeros
Console.WriteLine("Digite o primeiro número (x):");
int x = Convert.ToInt32(Console.ReadLine());

Console.WriteLine("Digite o segundo número (y):");
int y = Convert.ToInt32(Console.ReadLine());

// Verifica se x é par ou não usando o operador condicional ternário
string resultadoX = x % 2 == 0 ? "par" : "ímpar";

// Verifica se y é par ou não usando o operador condicional ternário
string resultadoY = y % 2 == 0 ? "par" : "ímpar";

//Imprime o resultado no console
Console.WriteLine($"O número x ({x}) é {resultadoX}");
Console.WriteLine($"O número y ({y}) é {resultadoY}");