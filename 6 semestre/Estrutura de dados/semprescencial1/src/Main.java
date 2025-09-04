public class Main {
    public static void main(String[] args) {
        Vetor turma = new Vetor();

        turma.inserir(new Aluno("João", 7.5));
        turma.inserir(new Aluno("Maria", 9.0));
        turma.inserir(new Aluno("Carlos", 5.5));

        System.out.println("Todos os alunos:");
        turma.listar();

        System.out.println("\nMaior nota: " + turma.maiorNota());
        System.out.println("Menor nota: " + turma.menorNota());
        System.out.println("Média da turma: " + turma.media());

        System.out.println("\nPesquisar 'Maria': " + turma.pesquisar("Maria"));
        System.out.println("Excluir 'Carlos': " + turma.excluir("Carlos"));

        System.out.println("\nAlunos após exclusão:");
        turma.listar();

        System.out.println("\nQuantidade de alunos: " + turma.quantidade());
    }
}