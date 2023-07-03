package ad_hoc_challenges;

import java.util.Arrays;
import java.util.Scanner;

public class Bee2473 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        String[] inputApostas = entrada.nextLine().split(" ");
        String[] inputSorteados = entrada.nextLine().split(" ");

        int[] apostas = Arrays.stream(inputApostas).mapToInt(Integer::parseInt).toArray();
        int[] sorteados = Arrays.stream(inputSorteados).mapToInt(Integer::parseInt).toArray();

        int qtd_acertos = 0;
        for (int i = 0; i < apostas.length; i++) {
           for (int j = 0; j < sorteados.length; j++) {
                if (apostas[i] == sorteados[j]) {
                    qtd_acertos += 1;
                }
           }
        } 

        String palavra = "";
        switch (qtd_acertos) {
            case 3:
                palavra = "terno";
                break;
            case 4:
                palavra = "quadra";
                break;
            case 5:
                palavra = "quina";
                break;
            case 6:
                palavra = "sena";
                break;
            default:
                palavra = "azar";
                break;
        }

        System.out.println(palavra);
        
        entrada.close();
    }
}
