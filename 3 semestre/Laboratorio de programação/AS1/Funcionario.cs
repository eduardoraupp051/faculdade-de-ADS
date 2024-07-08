using System;
using System.Collections.Generic;

// Define a classe abstrata Funcionario
public abstract class Funcionario
{
    // Propriedades públicas para armazenar o nome, a matrícula do funcionário e uma lista de projetos
    public string Nome { get; set; }
    public int Matricula { get; set; }
    public List<string> Projetos { get; set; }

    // Construtor da classe Funcionario
    public Funcionario(string nome, int matricula)
    {
        Nome = nome; // Inicializa o nome do funcionário
        Matricula = matricula; // Inicializa a matrícula do funcionário
        Projetos = new List<string>(); // Inicializa a lista de projetos
    }

    // Método abstrato para calcular o salário do funcionário
    public abstract double CalcularSalario();

    // Método abstrato para exibir as informações do funcionário
    public abstract void ExibirInformacoes();

    // Método para adicionar um projeto à lista de projetos
    public void AdicionarProjeto(string projeto)
    {
        Projetos.Add(projeto); // Adiciona o projeto fornecido à lista de projetos
    }

    // Método sobrecarregado para adicionar uma lista de projetos
    public void AdicionarProjeto(List<string> projetos)
    {
        Projetos.AddRange(projetos); // Adiciona cada projeto da lista fornecida à lista de projetos
    }
}
