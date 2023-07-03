package adHocChallenges;

import java.util.Scanner;

public class Bee2455 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int p1 = entrada.nextInt();
        int c1 = entrada.nextInt();
        int p2 = entrada.nextInt();
        int c2 = entrada.nextInt();

        int resultado = p1 * c1 == p2 * c2 ? 0: p1 * c1 < p2 * c2 ? 1: -1; 

        System.out.println(resultado);

        entrada.close();
    }
}
