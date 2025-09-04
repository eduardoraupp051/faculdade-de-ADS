public class Vetor {
    private Aluno[] alunos;
    private int tamanho;

    // Construtor com capacidade inicial 10
    public Vetor() {
        this.alunos = new Aluno[10];
        this.tamanho = 0;
    }

    // Inserir aluno no final
    public void inserir(Aluno aluno) {
        if (tamanho == alunos.length) {
            aumentarCapacidade();
        }
        alunos[tamanho] = aluno;
        tamanho++;
    }

    // Listar todos os alunos
    public void listar() {
        for (int i = 0; i < tamanho; i++) {
            System.out.println(alunos[i]);
        }
    }

    // Exibir aluno com maior nota
    public Aluno maiorNota() {
        if (tamanho == 0) return null;
        Aluno maior = alunos[0];
        for (int i = 1; i < tamanho; i++) {
            if (alunos[i].getNota() > maior.getNota()) {
                maior = alunos[i];
            }
        }
        return maior;
    }

    // Exibir aluno com menor nota
    public Aluno menorNota() {
        if (tamanho == 0) return null;
        Aluno menor = alunos[0];
        for (int i = 1; i < tamanho; i++) {
            if (alunos[i].getNota() < menor.getNota()) {
                menor = alunos[i];
            }
        }
        return menor;
    }

    // Calcular média da turma
    public double media() {
        if (tamanho == 0) return 0;
        double soma = 0;
        for (int i = 0; i < tamanho; i++) {
            soma += alunos[i].getNota();
        }
        return soma / tamanho;
    }

    // Pesquisar aluno por nome
    public boolean pesquisar(String nome) {
        for (int i = 0; i < tamanho; i++) {
            if (alunos[i].getNome().equalsIgnoreCase(nome)) {
                return true;
            }
        }
        return false;
    }

    // Excluir aluno por nome
    public boolean excluir(String nome) {
        for (int i = 0; i < tamanho; i++) {
            if (alunos[i].getNome().equalsIgnoreCase(nome)) {
                // desloca elementos para a esquerda
                for (int j = i; j < tamanho - 1; j++) {
                    alunos[j] = alunos[j + 1];
                }
                alunos[tamanho - 1] = null;
                tamanho--;
                return true;
            }
        }
        return false;
    }

    // Exibir quantidade de alunos
    public int quantidade() {
        return tamanho;
    }

    // Aumentar a capacidade do vetor (duplica)
    private void aumentarCapacidade() {
        Aluno[] novo = new Aluno[alunos.length * 2];
        for (int i = 0; i < alunos.length; i++) {
            novo[i] = alunos[i];
        }
        alunos = novo;
    }
}
