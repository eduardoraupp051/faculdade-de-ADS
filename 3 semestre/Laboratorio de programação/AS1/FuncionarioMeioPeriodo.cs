using System;

// Define a classe FuncionarioMeioPeriodo que herda da classe abstrata Funcionario e implementa a interface IBonus
public class FuncionarioMeioPeriodo : Funcionario, IBonus
{
    // Variáveis privadas para armazenar o salário por hora e o número de horas trabalhadas
    private double SalarioPorHora;
    private int HorasTrabalhadas;

    // Construtor da classe FuncionarioMeioPeriodo
    public FuncionarioMeioPeriodo(string nome, int matricula, double salarioPorHora, int horasTrabalhadas)
        : base(nome, matricula) // Chama o construtor da classe base Funcionario
    {
        SalarioPorHora = salarioPorHora; // Inicializa o salário por hora
        HorasTrabalhadas = horasTrabalhadas; // Inicializa o número de horas trabalhadas
    }

    // Implementação do método abstrato CalcularSalario da classe Funcionario
    public override double CalcularSalario()
    {
        return SalarioPorHora * HorasTrabalhadas; // Calcula e retorna o salário com base no salário por hora e horas trabalhadas
    }

    // Implementação do método abstrato ExibirInformacoes da classe Funcionario
    public override void ExibirInformacoes()
    {
        // Exibe as informações do funcionário
        Console.WriteLine($"Nome: {Nome}, Matrícula: {Matricula}, Salário por Hora: {SalarioPorHora:C}, Horas Trabalhadas: {HorasTrabalhadas}");
    }

    // Implementação do método CalcularBonus da interface IBonus
    public double CalcularBonus()
    {
        return CalcularSalario() * 0.05; // Calcula e retorna o bônus que é 5% do salário total
    }
}
