import java.util.*; // inclui Scanner

class Matriz {
    int[][] dados;
    int linhas, colunas;

    Matriz(int l, int c) {
        linhas = l;
        colunas = c;
        dados = new int[l][c];
    }

    void preencherManual(Scanner sc) {
        for (int i = 0; i < linhas; i++) {
            for (int j = 0; j < colunas; j++) {
                System.out.print("Digite o valor para [" + i + "][" + j + "]: ");
                dados[i][j] = sc.nextInt();
            }
        }
    }

    // Preencher automático com sequência (1,2,3,...)
    void preencherAutomatico() {
        int valor = 1;
        for (int i = 0; i < linhas; i++) {
            for (int j = 0; j < colunas; j++) {
                dados[i][j] = valor++;
            }
        }
    }

    void removerElemento(int i, int j) {
        if (i >= 0 && i < linhas && j >= 0 && j < colunas) {
            dados[i][j] = 0;
        }
    }

    void exibir() {
        for (int i = 0; i < linhas; i++) {
            for (int j = 0; j < colunas; j++) {
                System.out.printf("%4d", dados[i][j]);
            }
            System.out.println();
        }
    }

    int[] achatar() {
        int[] v = new int[linhas * colunas];
        int k = 0;
        for (int i = 0; i < linhas; i++) {
            for (int j = 0; j < colunas; j++) {
                v[k++] = dados[i][j];
            }
        }
        return v;
    }

    void reconstruir(int[] v) {
        int k = 0;
        for (int i = 0; i < linhas; i++) {
            for (int j = 0; j < colunas; j++) {
                dados[i][j] = v[k++];
            }
        }
    }
}
