package StringChallenges;

import java.util.Scanner;

public class Bee1871 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        while (true) {
            String valores = entrada.nextLine();    
            String[] vetor_valores = valores.split(" ");
            int M = Integer.parseInt(vetor_valores[0]);
            int N = Integer.parseInt(vetor_valores[1]);
            int somaValores = M + N;
        
            if (somaValores == 0) {
                break;
            } else {
                String stringSomaValores = Integer.toString(somaValores);
                char[] vetor_caracteres = stringSomaValores.toCharArray();
                String resultado = "";
        
                for (int i = 0; i < vetor_caracteres.length; i++) {
                    if (vetor_caracteres[i] != '0') {
                        resultado += vetor_caracteres[i];
                    }
                }
        
                System.out.println(resultado);
            }
        } 
        entrada.close();  
    }
}