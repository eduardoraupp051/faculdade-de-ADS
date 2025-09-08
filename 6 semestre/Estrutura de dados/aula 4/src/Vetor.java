import java.util.Arrays;

public class Vetor{
    private String[] elementos;
    private int tamanho;

    public Vetor(int capacidade){
        this.elementos = new String[capacidade];
        this.tamanho = 0;
    }

    public int tamanho(){
        return this.tamanho;
    }

    public void inserir(String elemento){

        if (tamanho == elementos.length) {
            aumentarCapacidade();
        }

        this.elementos[tamanho] = elemento;
        tamanho++;

    }

    public void inserir(String elemento, int indice){
        if(indice < 0 || indice > tamanho){
            System.out.println("Índice inválido");
        }else if(tamanho < elementos.length){
            for(int i = tamanho; i > indice; i--){
                elementos[i] = elementos[i - 1];
            }
            this.elementos[indice] = elemento;
            tamanho++;
        }
    }

    public void remover(int indice){
        if(indice >=0 && indice < tamanho){

            for(int i = indice; i < tamanho; i++){
                this.elementos[i] = this.elementos[i+1];
            }

            this.elementos[tamanho] = null;
            tamanho--;
        }
    }

    public String obter(int indice){
        if(indice >= 0 || indice < tamanho){
            return this.elementos[indice];
        }
        return null;
    }

    public void aumentarCapacidade(){
            String[] novoVetor = new String[elementos.length * 2];
            for(int i = 0; i < tamanho; i++){
                novoVetor[i] = elementos[i];
            }

            elementos = novoVetor;
    }


//    @Override
//    public String toString() {
//        return Arrays.toString(elementos);
//    }
    public String toString() {
        String texto = "[";

        for(int i = 0; i < tamanho; i++){
            texto += elementos[i];
            if(i != tamanho - 1){
                texto += ", ";
            }
        }
        texto += "]";
        return texto;
    }
}
