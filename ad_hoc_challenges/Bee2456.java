package ad_hoc_challenges;
import java.util.Scanner;

public class Bee2456 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);  
        String[] stringValores = entrada.nextLine().split(" ");
        int[] valores = new int[stringValores.length];

        for (int i = 0; i < stringValores.length; i++) {
            valores[i] = Integer.parseInt(stringValores[i]);
        }

        boolean ascendingOrder = false;
        for (int i = 0; i < valores.length - 1; i++) {
            if (valores[i] < valores[i + 1]) {
                ascendingOrder = true;
            } else {
                ascendingOrder = false;
                break;
            }
        }
        
        boolean descendingOrder = false;
        if (!ascendingOrder) {
            for (int i = 0; i < valores.length - 1; i++) {
                if (valores[i] > valores[i + 1]) {
                    descendingOrder = true;
                } else {
                    descendingOrder = false;
                    break;
                }
            }
        } 

        if (ascendingOrder) {
            System.out.println("C");
        } else if (descendingOrder) {
            System.out.println("D");
        } else {
            System.out.println("N");
        }
  
        entrada.close();
    }
}
