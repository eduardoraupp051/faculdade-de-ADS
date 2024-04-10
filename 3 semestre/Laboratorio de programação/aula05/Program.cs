
// Console.WriteLine("## instrução if##");


// Console.WriteLine("cliente especial (S/N)");
// var resposta = Console.ReadLine();

// if (resposta == "s")
// {
//     Console.WriteLine("DEsconto de 10%");
// }

// Console.WriteLine("cliente especial (true/false)");
// var resposta = Convert.ToBoolean(Console.ReadLine());

// if (resposta)
// {
//     Console.WriteLine("DEsconto de 10%");
// }

// Console.WriteLine("informa o valor de X");
// int x = Convert.ToInt32(Console.ReadLine());

// Console.WriteLine("informe o valor de y");
// int y = Convert.ToInt32(Console.ReadLine());

// if (x > y)
// {
//     Console.WriteLine("X é maior que Y");
// }

// else{
//     if (x < y)
//     {
//         Console.WriteLine("x é menor que Y");
//     }

//     else
//     {
//         Console.WriteLine("X é igual a Y");
//     }

// }


// Console.WriteLine("informe a nota do aluno: ");
// var nota = Convert.ToInt32(Console.ReadLine());

// if (nota > 5)
// {
//     Console.WriteLine("aluno aprovado");
// }

// else
// {
//     Console.WriteLine("aluno reprovado");
// }

// using System.Net;

// int compra = 600;
// Console.WriteLine("valor da compra 600 reais");
// Console.WriteLine("informe o numero de parcelas (1 a 3)");
// var numParcelas = Convert.ToInt32(Console.ReadLine());
// switch (numParcelas)
// {
//     case 1:
//         Console.WriteLine($"prestaçao {compra / numParcelas}");
//         break;

//     case 2:
//         Console.WriteLine($"prestaçao {compra / numParcelas}");
//         break;

//     case 3:
//         Console.WriteLine($"prestaçao {compra / numParcelas}");
//         break;

//     default:
//         Console.WriteLine("valor invalido, informe 1, 2 ou 3");
//         break;

// }

// Console.WriteLine("informe o nome do mes");
// var mes = Console.ReadLine().ToLower();

// switch (mes)
// {
//     case "janeiro":
//     case "março":
//     case "maio":
//     case "julho":
//     case "agosto":
//     case "outubro":
//     case "dezembro":
//         Console.WriteLine("esse mes tem 31 dias");
//         break;
//     case "fevereiro":
//         Console.WriteLine("esse mes tem 29 dias");
//         break;
//     default:
//         Console.WriteLine("esse mes tem 30 dias");
//         break;
// }

// var i = 0;

// do
// {
//     Console.WriteLine($"i = {i}");
//     i++;

// }
// while (i < 2);


// int contador = 1;
// Console.WriteLine("digite um numero");
// int numero = Convert.ToInt32(Console.ReadLine());
// Console.WriteLine($"tabuada do {numero}");

// while(contador < 11)
// {
//     Console.WriteLine($"{numero} X {contador} = {numero + contador}");
//     contador++;

// }

int numero, resultado;

Console.WriteLine("informe um numero inteiro");

numero = Convert.ToInt32(Console.ReadLine());

for (int i = 1; i < 10; i++)
{
    resultado = numero * i;
    Console.WriteLine(numero + " x " + i + "=" + resultado);

}

