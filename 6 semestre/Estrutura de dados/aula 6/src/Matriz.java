public class Matriz {
    private int linhas;
    private int colunas;
    private int[][] matriz;

    public Matriz(int linhas, int colunas){
        this.linhas = linhas;
        this.colunas = colunas;
        matriz = new int[linhas][colunas];
    }
    public void setMatriz(int [][] matriz){
        this.matriz = matriz;
    }

    public int obterMaior(){
        int maior = matriz[0][0];

        for(int i = 0; i < linhas; i++){
            for(int j = 0; j < colunas; j++){
                if(matriz[i][j] > maior){
                    maior = matriz[i][j];
                }
            }
        }
        return maior;
    }

   

}
