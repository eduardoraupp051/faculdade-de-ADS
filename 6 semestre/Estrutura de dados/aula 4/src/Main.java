//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        //Declarando um vetor
        String[] frutas;
        //Inicializando o vetor frutas
        frutas = new String[4];

        //String[] frutas2 = new String[5];

        frutas[0] = "Banana";
        frutas[1] = "Maça";

        //System.out.println(frutas[0]);

        String[] frutas3 = {"Maça", "Abacaxi", "Melancia"};

//        for(int i = 0; i < frutas.length; i++){
//            if(frutas[i] != null){
//                System.out.println(frutas[i]);
//            }
//        }

//        for(String fruta : frutas3){
//            System.out.println(fruta);
//        }

        int[][] numeros = new int[2][3];

//        System.out.println("Linhas: " + numeros.length);
//        System.out.println("Colunas: " + numeros[0].length);

        numeros[0][0] = 1;
        numeros[0][1] = 2;
        numeros[0][2] = 3;
        numeros[1][0] = 4;
        numeros[1][1] = 5;
        numeros[1][2] = 6;

        int [][] matriz2 = {
                {1,1,1},
                {2,2,2},
                {4,5,6}
        };


//        for(int i = 0; i < numeros.length; i++){
//            for(int j = 0; j < numeros[i].length; j++){
//                System.out.println("Linha "+ (i + 1) + " Coluna " + (j + 1) + " = " + numeros[i][j]);
//            }
//        }

//        for(int i = 0; i < matriz2.length; i++){
//
//            for(int j = 0; j < matriz2[i].length; j++){
//                System.out.print(matriz2[i][j] + " | ");
//            }
//            System.out.println();
//        }

        Vetor nomes = new Vetor(4);

        nomes.inserir("A");
        nomes.inserir("B");
        nomes.inserir("C");


        nomes.inserir("F");
        nomes.inserir("G");
        System.out.println(nomes);

        //System.out.println(nomes.obter(5));

       // nomes.remover(0);
        System.out.println(nomes);


    }
}