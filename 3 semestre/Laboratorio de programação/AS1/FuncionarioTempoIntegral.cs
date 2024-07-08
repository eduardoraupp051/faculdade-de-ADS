using System;

// Define a classe FuncionarioTempoIntegral que herda da classe abstrata Funcionario e implementa a interface IBonus
public class FuncionarioTempoIntegral : Funcionario, IBonus
{
    // Variável privada para armazenar o salário mensal
    private double SalarioMensal;

    // Construtor da classe FuncionarioTempoIntegral
    public FuncionarioTempoIntegral(string nome, int matricula, double salarioMensal)
        : base(nome, matricula) // Chama o construtor da classe base Funcionario
    {
        SalarioMensal = salarioMensal; // Inicializa o salário mensal
    }

    // Implementação do método abstrato CalcularSalario da classe Funcionario
    public override double CalcularSalario()
    {
        return SalarioMensal; // Retorna o salário mensal
    }

    // Implementação do método abstrato ExibirInformacoes da classe Funcionario
    public override void ExibirInformacoes()
    {
        // Exibe as informações do funcionário
        Console.WriteLine($"Nome: {Nome}, Matrícula: {Matricula}, Salário Mensal: {SalarioMensal:C}");
    }

    // Implementação do método CalcularBonus da interface IBonus
    public double CalcularBonus()
    {
        return SalarioMensal * 0.10; // Calcula e retorna o bônus que é 10% do salário mensal
    }
}
