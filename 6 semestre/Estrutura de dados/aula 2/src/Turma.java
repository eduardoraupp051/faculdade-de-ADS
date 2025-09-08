public class Turma {
    private int id;
    private String nome;
    public Professor professor;
    private Aluno[] alunos;
    private int contaAlunos;

    public Turma(int numeroAlunos){
        this.alunos = new Aluno[numeroAlunos];
        this.contaAlunos = 0;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void inserirAluno(Aluno aluno){
        if (contaAlunos < alunos.length){
            this.alunos[contaAlunos] = aluno;
            contaAlunos++;
        }
    }
    public void listar(){
        for(int i = 0; i < contaAlunos; i++){
            System.out.println("Aluno " + (i + 1) + ": " +alunos[i]);
        }
    }
}
