using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        // Cria uma nova instância da classe Empresa
        Empresa empresa = new Empresa();
        bool continuar = true;

        // Loop principal do menu interativo
        while (continuar)
        {
            // Exibe o menu de opções
            Console.WriteLine("\nMenu:");
            Console.WriteLine("1. Adicionar funcionário de tempo integral");
            Console.WriteLine("2. Adicionar funcionário de meio período");
            Console.WriteLine("3. Remover funcionário");
            Console.WriteLine("4. Exibir informações de todos os funcionários");
            Console.WriteLine("5. Adicionar projeto(s) a um funcionário");
            Console.WriteLine("6. Sair");
            Console.Write("Selecione uma opção: ");

            // Lê a opção escolhida pelo usuário e tenta convertê-la para um inteiro
            if (int.TryParse(Console.ReadLine(), out int opcao))
            {
                // Executa a ação correspondente à opção escolhida
                switch (opcao)
                {
                    case 1:
                        // Adiciona um funcionário de tempo integral
                        AdicionarFuncionarioTempoIntegral(empresa);
                        break;
                    case 2:
                        // Adiciona um funcionário de meio período
                        AdicionarFuncionarioMeioPeriodo(empresa);
                        break;
                    case 3:
                        // Remove um funcionário
                        RemoverFuncionario(empresa);
                        break;
                    case 4:
                        // Exibe informações de todos os funcionários
                        empresa.ExibirFuncionarios();
                        break;
                    case 5:
                        // Adiciona projetos a um funcionário
                        AdicionarProjeto(empresa);
                        break;
                    case 6:
                        // Sai do programa
                        continuar = false;
                        break;
                    default:
                        // Informa ao usuário que a opção escolhida é inválida
                        Console.WriteLine("Opção inválida!");
                        break;
                }
            }
            else
            {
                // Informa ao usuário que a entrada é inválida e não é um número
                Console.WriteLine("Entrada inválida! Por favor, insira um número.");
            }
        }
    }

    // Método para adicionar um funcionário de tempo integral
    static void AdicionarFuncionarioTempoIntegral(Empresa empresa)
    {
        Console.Write("Nome: ");
        string nome = Console.ReadLine();
        Console.Write("Matrícula: ");
        // Tenta converter a entrada para matrícula em inteiro
        if (int.TryParse(Console.ReadLine(), out int matricula))
        {
            Console.Write("Salário Mensal: ");
            // Tenta converter a entrada para salário mensal em double
            if (double.TryParse(Console.ReadLine(), out double salarioMensal))
            {
                // Cria um novo funcionário de tempo integral e o adiciona à empresa
                FuncionarioTempoIntegral funcionario = new FuncionarioTempoIntegral(nome, matricula, salarioMensal);
                empresa.AdicionarFuncionario(funcionario);
            }
            else
            {
                // Informa ao usuário que a entrada para salário mensal é inválida
                Console.WriteLine("Entrada inválida para salário mensal.");
            }
        }
        else
        {
            // Informa ao usuário que a entrada para matrícula é inválida
            Console.WriteLine("Entrada inválida para matrícula.");
        }
    }

    // Método para adicionar um funcionário de meio período
    static void AdicionarFuncionarioMeioPeriodo(Empresa empresa)
    {
        Console.Write("Nome: ");
        string nome = Console.ReadLine();
        Console.Write("Matrícula: ");
        // Tenta converter a entrada para matrícula em inteiro
        if (int.TryParse(Console.ReadLine(), out int matricula))
        {
            Console.Write("Salário por Hora: ");
            // Tenta converter a entrada para salário por hora em double
            if (double.TryParse(Console.ReadLine(), out double salarioPorHora))
            {
                Console.Write("Horas Trabalhadas: ");
                // Tenta converter a entrada para horas trabalhadas em inteiro
                if (int.TryParse(Console.ReadLine(), out int horasTrabalhadas))
                {
                    // Cria um novo funcionário de meio período e o adiciona à empresa
                    FuncionarioMeioPeriodo funcionario = new FuncionarioMeioPeriodo(nome, matricula, salarioPorHora, horasTrabalhadas);
                    empresa.AdicionarFuncionario(funcionario);
                }
                else
                {
                    // Informa ao usuário que a entrada para horas trabalhadas é inválida
                    Console.WriteLine("Entrada inválida para horas trabalhadas.");
                }
            }
            else
            {
                // Informa ao usuário que a entrada para salário por hora é inválida
                Console.WriteLine("Entrada inválida para salário por hora.");
            }
        }
        else
        {
            // Informa ao usuário que a entrada para matrícula é inválida
            Console.WriteLine("Entrada inválida para matrícula.");
        }
    }

    // Método para remover um funcionário
    static void RemoverFuncionario(Empresa empresa)
    {
        Console.Write("Matrícula do funcionário a ser removido: ");
        // Tenta converter a entrada para matrícula em inteiro
        if (int.TryParse(Console.ReadLine(), out int matricula))
        {
            // Remove o funcionário com a matrícula fornecida
            empresa.RemoverFuncionario(matricula);
        }
        else
        {
            // Informa ao usuário que a entrada para matrícula é inválida
            Console.WriteLine("Entrada inválida para matrícula.");
        }
    }

    // Método para adicionar projetos a um funcionário
    static void AdicionarProjeto(Empresa empresa)
    {
        Console.Write("Matrícula do funcionário: ");
        // Tenta converter a entrada para matrícula em inteiro
        if (int.TryParse(Console.ReadLine(), out int matricula))
        {
            // Obtém o funcionário com a matrícula fornecida
            var funcionario = empresa.ObterFuncionarioPorMatricula(matricula);
            if (funcionario != null)
            {
                Console.Write("Quantos projetos deseja adicionar? ");
                // Tenta converter a entrada para quantidade de projetos em inteiro
                if (int.TryParse(Console.ReadLine(), out int quantidade))
                {
                    List<string> projetos = new List<string>();
                    for (int i = 0; i < quantidade; i++)
                    {
                        Console.Write($"Nome do projeto {i + 1}: ");
                        projetos.Add(Console.ReadLine());
                    }
                    // Adiciona os projetos ao funcionário
                    funcionario.AdicionarProjeto(projetos);
                }
                else
                {
                    // Informa ao usuário que a entrada para quantidade de projetos é inválida
                    Console.WriteLine("Entrada inválida para quantidade de projetos.");
                }
            }
            else
            {
                // Informa ao usuário que o funcionário não foi encontrado
                Console.WriteLine("Funcionário não encontrado.");
            }
        }
        else
        {
            // Informa ao usuário que a entrada para matrícula é inválida
            Console.WriteLine("Entrada inválida para matrícula.");
        }
    }
}
