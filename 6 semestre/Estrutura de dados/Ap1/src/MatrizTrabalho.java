import java.util.*; // já inclui Scanner

public class MatrizTrabalho {
    static Scanner sc = new Scanner(System.in);

    // Bubble Sort (iterativo)
    static void bubbleSort(int[] v) {
        for (int i = 0; i < v.length - 1; i++) {
            for (int j = 0; j < v.length - 1 - i; j++) {
                if (v[j] > v[j + 1]) {
                    int aux = v[j];
                    v[j] = v[j + 1];
                    v[j + 1] = aux;
                }
            }
        }
    }

    // Merge Sort (recursivo)
    static void mergeSort(int[] v, int ini, int fim) {
        if (ini >= fim) return;
        int meio = (ini + fim) / 2;
        mergeSort(v, ini, meio);
        mergeSort(v, meio + 1, fim);
        intercalar(v, ini, meio, fim);
    }

    static void intercalar(int[] v, int ini, int meio, int fim) {
        int[] aux = new int[fim - ini + 1];
        int i = ini, j = meio + 1, k = 0;
        while (i <= meio && j <= fim) {
            if (v[i] <= v[j]) aux[k++] = v[i++];
            else aux[k++] = v[j++];
        }
        while (i <= meio) aux[k++] = v[i++];
        while (j <= fim) aux[k++] = v[j++];
        for (k = 0; k < aux.length; k++) v[ini + k] = aux[k];
    }

    public static void main(String[] args) {
        System.out.print("Digite o número de linhas: ");
        int l = sc.nextInt();
        System.out.print("Digite o número de colunas: ");
        int c = sc.nextInt();

        Matriz m = new Matriz(l, c);

        int op;
        for (;;) {
            System.out.println("\nMENU:");
            System.out.println("1 - Preencher manual");
            System.out.println("2 - Preencher automático (sequência numérica)");
            System.out.println("3 - Exibir matriz");
            System.out.println("4 - Remover elemento");
            System.out.println("5 - Ordenar BubbleSort");
            System.out.println("6 - Ordenar MergeSort");
            System.out.println("0 - Sair");
            System.out.print("Opção: ");
            op = sc.nextInt();

            if (op == 0) break;

            switch (op) {
                case 1 -> m.preencherManual(sc);
                case 2 -> m.preencherAutomatico();
                case 3 -> m.exibir();
                case 4 -> {
                    System.out.print("Linha: "); int i = sc.nextInt();
                    System.out.print("Coluna: "); int j = sc.nextInt();
                    m.removerElemento(i, j);
                }
                case 5 -> {
                    int[] v = m.achatar();
                    bubbleSort(v);
                    m.reconstruir(v);
                }
                case 6 -> {
                    int[] v = m.achatar();
                    mergeSort(v, 0, v.length - 1);
                    m.reconstruir(v);
                }
                default -> System.out.println("Opção inválida!");
            }
        }
    }
}
