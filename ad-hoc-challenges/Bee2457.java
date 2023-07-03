package adHocChallenges;

import java.util.Scanner;
import java.util.Locale;

public class Bee2457 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner entrada = new Scanner(System.in);
        String caractere = entrada.next();
        entrada.nextLine();
        String[] texto = entrada.nextLine().split(" ");

        int qtdPalavras= 0;
        int qntLetrasPalavra = 0;
 
        for (int i = 0; i < texto.length; i++) {
            for (int j = 0; j < texto[i].length(); j++) {
                String caractereDaVez = texto[i].charAt(j) + "";
                if (caractereDaVez.equals(caractere)) {
                    qntLetrasPalavra++;
                    break;
                } 
            }
            qtdPalavras++;
        }
        
        double porcentagem = (qntLetrasPalavra * 100.0) / qtdPalavras;
        System.out.printf("%.1f", porcentagem);
        System.out.println();
        entrada.close();
    }
}