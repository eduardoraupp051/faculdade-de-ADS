
//                  EXERCICIO 1
// using System;

// class Program
// {
//     static void Main(string[] args)
//     {
//         Console.WriteLine("Encontre o maior dentre 3 números:");

//         // Solicita ao usuário que insira os três números
//         Console.Write("Primeiro Número: ");
//         int num1 = int.Parse(Console.ReadLine());

//         Console.Write("Segundo Número: ");
//         int num2 = int.Parse(Console.ReadLine());

//         Console.Write("Terceiro Número: ");
//         int num3 = int.Parse(Console.ReadLine());

//         // Verifica qual número é o maior
//         if (num1 > num2 && num1 > num3)
//         {
//             Console.WriteLine($"O primeiro número: {num1} é o maior");
//         }
//         else if (num2 > num1 && num2 > num3)
//         {
//             Console.WriteLine($"O segundo número: {num2} é o maior");
//         }
//         else
//         {
//             Console.WriteLine($"O terceiro número: {num3} é o maior");
//         }
//     }
// }


//                  EXERCICIO 2
// using System;

// class Program
// {
//     static void Main(string[] args)
//     {
//         // Loop usando while
//         Console.WriteLine("Loop usando while:");
//         int i = 1;
//         int sumWhile = 0;
//         while (i <= 10)
//         {
//             Console.Write(i + " ");
//             sumWhile += i;
//             i++;
//         }
//         Console.WriteLine();
//         Console.WriteLine("A soma dos números é: " + sumWhile);
//         Console.WriteLine();

//         // Loop usando do-while
//         Console.WriteLine("Loop usando do-while:");
//         int j = 1;
//         int sumDoWhile = 0;
//         do
//         {
//             Console.Write(j + " ");
//             sumDoWhile += j;
//             j++;
//         } while (j <= 10);
//         Console.WriteLine();
//         Console.WriteLine("A soma dos números é: " + sumDoWhile);
//         Console.WriteLine();

//         // Loop usando for
//         Console.WriteLine("Loop usando for:");
//         int sumFor = 0;
//         for (int k = 1; k <= 10; k++)
//         {
//             Console.Write(k + " ");
//             sumFor += k;
//         }
//         Console.WriteLine();
//         Console.WriteLine("A soma dos números é: " + sumFor);
//     }
// }


//                  EXERCICIO 3
// using System;

// class Program
// {
//     static void Main(string[] args)
//     {
//         while (true)
//         {
//             Console.Write("Digite um número natural maior que zero (ou 0 para sair): ");
//             int numero = int.Parse(Console.ReadLine());

//             if (numero <= 0)
//             {
//                 Console.WriteLine("O número digitado não é maior que zero. Tente novamente.");
//                 continue;
//             }

//             Console.WriteLine($"Tabela de multiplicação para o número {numero}:");
//             for (int i = 1; i <= 10; i++)
//             {
//                 Console.WriteLine($"{numero} x {i} = {numero * i}");
//             }

//             Console.WriteLine();

//             Console.Write("Deseja verificar outra tabela de multiplicação? (S/N): ");
//             string resposta = Console.ReadLine().ToUpper();
//             if (resposta != "S")
//             {
//                 break;
//             }
//         }
//     }
// }


//                  EXERCICIO 4


//                      1. Incrementando 2 em cada passo:
// using System;

// class Program
// {
//     static void Main(string[] args)
//     {
//         Console.WriteLine("Números pares de 10 a 20 (excluindo 16) incrementando 2 em cada passo:");
//         for (int i = 10; i <= 20; i += 2)
//         {
//             if (i == 16)
//                 continue;
//             Console.WriteLine(i);
//         }
//     }
// }



//                  2. Incrementando 1 em cada passo:
// using System;

// class Program
// {
//     static void Main(string[] args)
//     {
//         Console.WriteLine("Números pares de 10 a 20 (excluindo 16) incrementando 1 em cada passo:");
//         for (int i = 10; i <= 20; i++)
//         {
//             if (i == 16 || i % 2 != 0)
//                 continue;
//             Console.WriteLine(i);
//         }
//     }
// }



//                  3. Com loop infinito (usando "break" e "continue"):
// using System;

// class Program
// {
//     static void Main(string[] args)
//     {
//         Console.WriteLine("Números pares de 10 a 20 (excluindo 16) usando loop infinito:");
//         int i = 10;
//         while (true)
//         {
//             if (i > 20)
//                 break;
//             if (i == 16)
//             {
//                 i++;
//                 continue;
//             }
//             Console.WriteLine(i);
//             i += 2;
//         }
//     }
// }


//                  EXERCICIO 5
// using System;

// class Program
// {
//     static void Main(string[] args)
//     {
//         Console.Write("Digite um número inteiro para calcular o fatorial: ");
//         int numero = int.Parse(Console.ReadLine());

//         // Verifica se o número é não-negativo
//         if (numero < 0)
//         {
//             Console.WriteLine("O fatorial não está definido para números negativos.");
//             return;
//         }

//         long fatorial = 1;
//         for (int i = 1; i <= numero; i++)
//         {
//             fatorial *= i;
//         }

//         Console.WriteLine($"O fatorial de {numero} é {fatorial}.");
//     }
// }


//              EXERCICIO 6
// using System;

// class Program
// {
//     static void Main(string[] args)
//     {
//         int multiplicador = 2;

//         do
//         {
//             int multiplicando = 1;
//             Console.WriteLine($"Tabela de multiplicação do {multiplicador}:");
//             do
//             {
//                 int resultado = multiplicador * multiplicando;
//                 Console.WriteLine($"{multiplicador} x {multiplicando} = {resultado}");
//                 multiplicando++;
//             } while (multiplicando <= 10);
//             Console.WriteLine();
//             multiplicador++;
//         } while (multiplicador <= 6);
//     }
// }


//                  EXERCICIO 7
// using System;

// class Program
// {
//     static void Main(string[] args)
//     {
//         while (true)
//         {
//             Console.Write("Digite a nota do aluno (0 a 10): ");
//             int nota = int.Parse(Console.ReadLine());

//             switch (nota)
//             {
//                 case 0:
//                 case 1:
//                 case 2:
//                 case 3:
//                 case 4:
//                     Console.WriteLine("Resultado da avaliação: F");
//                     break;
//                 case 5:
//                     Console.WriteLine("Resultado da avaliação: E");
//                     break;
//                 case 6:
//                     Console.WriteLine("Resultado da avaliação: C");
//                     break;
//                 case 7:
//                 case 8:
//                     Console.WriteLine("Resultado da avaliação: B");
//                     break;
//                 case 9:
//                 case 10:
//                     Console.WriteLine("Resultado da avaliação: A+");
//                     break;
//                 default:
//                     Console.WriteLine("Nota inválida. Tente novamente.");
//                     break;
//             }

//             Console.Write("Deseja avaliar outro aluno? (S/N): ");
//             string resposta = Console.ReadLine().ToUpper();
//             if (resposta != "S")
//             {
//                 break;
//             }
//         }
//     }
// }


//                  EXERCICIO 8
