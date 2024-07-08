using System;
using System.Collections.Generic;
using System.Linq;

// Define a classe Empresa
public class Empresa
{
    // Lista privada para armazenar os funcionários
    private List<Funcionario> funcionarios;

    // Construtor da classe Empresa
    public Empresa()
    {
        // Inicializa a lista de funcionários
        funcionarios = new List<Funcionario>();
    }

    // Método para adicionar um funcionário à lista
    public void AdicionarFuncionario(Funcionario funcionario)
    {
        funcionarios.Add(funcionario);
    }

    // Método para remover um funcionário da lista com base na matrícula
    public void RemoverFuncionario(int matricula)
    {
        // Encontra o primeiro funcionário com a matrícula fornecida
        var funcionario = funcionarios.FirstOrDefault(f => f.Matricula == matricula);
        // Se o funcionário for encontrado, remove-o da lista
        if (funcionario != null)
        {
            funcionarios.Remove(funcionario);
        }
    }

    // Método para exibir as informações de todos os funcionários
    public void ExibirFuncionarios()
    {
        // Itera sobre a lista de funcionários e exibe suas informações
        foreach (var funcionario in funcionarios)
        {
            funcionario.ExibirInformacoes();
        }
    }

    // Método para obter um funcionário por matrícula
    public Funcionario ObterFuncionarioPorMatricula(int matricula)
    {
        // Retorna o primeiro funcionário com a matrícula fornecida ou null se não encontrado
        return funcionarios.FirstOrDefault(f => f.Matricula == matricula);
    }
}
