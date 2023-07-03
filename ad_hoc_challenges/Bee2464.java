package ad_hoc_challenges;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Bee2464 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        Map<Character, Integer> hashMap = new HashMap<>();

        int valor = 0;
        for (char letra = 'a'; letra <= 'z'; letra++) {
            hashMap.put(letra, valor);
            valor++;
        }
        
        char[] permutacao = entrada.nextLine().toCharArray();
        char[] fraseCriptografada = entrada.nextLine().toCharArray();

        String fraseDescriptografada = "";

        for (int i = 0; i < fraseCriptografada.length; i++) {
            int indice = hashMap.get(fraseCriptografada[i]); 
            fraseDescriptografada += permutacao[indice];
        }

        System.out.println(fraseDescriptografada);
        
        entrada.close();
    }
}