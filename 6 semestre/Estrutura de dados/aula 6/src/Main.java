import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        int[] numeros = {9, 3, 2, 110, 43, 22};

        Ordenacao.bubbleSort(numeros);

        System.out.println(Arrays.toString(numeros));

        Funcionario[] funcionarios = new Funcionario[5];

        Funcionario f1 = new Funcionario();
        f1.nome = "Maurício";
        f1.salario = 20000;

        Funcionario f2 = new Funcionario();
        f1.nome = "Antônio";
        f1.salario = 10000;

        funcionarios[0] = f1;
        funcionarios[1] = f2;


        String nome1 = "Ana";
        String nome2 = "Adriana";
        if (nome1.compareTo(nome2) > 0){
            System.out.println("Sim");
        }
        System.out.println(nome1.compareTo(nome2));


        Matriz matriz = new Matriz(3,3);

        int[][] m1 = {
                {10, 20 ,30},
                {12, 22, 5},
                {99, 1, 0}
        };

        matriz.setMatriz(m1);
        System.out.println(matriz.obterMaior());
    }
}