public class Ordenacao {


    public static void bubbleSort(int[] vetor){
        int n = vetor.length;

        for(int i = 0; i < n - 1; i++){
            for(int j = 0; j < n - 1 - i; j++){
                if(vetor[j] > vetor[j + 1]){
                    int temp = vetor[j];
                    vetor[j] = vetor[j + 1];
                    vetor[j + 1] = temp;
                }
            }
        }

    }

    public static void selectionSort(int[] vetor){
        int n = vetor.length;
        for(int i = 0; i < n -1; i++){
            int indiceMinimo = i;
            for(int j = i + 1; j < n; j++){
                if(vetor[j] < vetor[indiceMinimo]){
                    indiceMinimo = j;
                }
            }
            int aux = vetor[indiceMinimo];
            vetor[indiceMinimo] = vetor[i];
            vetor[i] = aux;
        }
    }

    public static void insertionSort(int[] vetor){
        int n = vetor.length;
        for(int i = 1; i < n; i++){
            int valor = vetor[i];
            int j = i - 1;

            while(j >= 0 && vetor[j] > valor){
                vetor[j + 1] = vetor[j];
                j--;
            }
            vetor[j + 1] = valor;
        }
    }


}
