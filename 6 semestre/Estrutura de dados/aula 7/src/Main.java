import java.util.Arrays;
import java.util.Random;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        //int respota = Recursiva.fibonacci(10);
        //System.out.println(respota);

        int[] vetor1 = {5, 2, 100, 1, 33, 80, 92, 32};

        int[] vetor2 = new int[100];

        Random r = new Random();

        for(int i = 0; i < vetor2.length; i++){
            vetor2[i] = r.nextInt(10000);
        }


        Recursiva.mergeSort(vetor2, 0, vetor2.length - 1);

        System.out.println(Arrays.toString(vetor2));

    }
}