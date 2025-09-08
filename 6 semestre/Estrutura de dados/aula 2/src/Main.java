//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {

        Professor pro1 = new Professor();
        pro1.setNome("Juliano");
        pro1.setEmail("juliano@gmail");

        Aluno aluno1 = new Aluno();
        aluno1.setNome("Antônio");
        aluno1.setEmail("antonio@gmail.com");

        Aluno aluno2 = new Aluno();
        aluno2.setNome("Ana");
        aluno2.setEmail("ana@gmail.com");

        Aluno aluno3 = new Aluno();
        aluno3.setNome("Adão");
        aluno3.setEmail("adao@gmail.com");

        Turma estruturas = new Turma(10);
        estruturas.professor = pro1;
        estruturas.setNome("Estruturas de Dados");
        estruturas.setId(54321);

        estruturas.inserirAluno(aluno1);
        estruturas.inserirAluno(aluno2);
        estruturas.inserirAluno(aluno3);

        System.out.println(estruturas.getNome());
        System.out.println(estruturas.getId());
        System.out.println(estruturas.professor);

        estruturas.listar();





    }
}