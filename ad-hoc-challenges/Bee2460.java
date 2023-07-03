package adHocChallenges;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Bee2460 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int qtdPessoasFila = scanner.nextInt();
        scanner.nextLine();
        String[] identificadores = scanner.nextLine().split(" ");
        int qtd_sairam = scanner.nextInt();
        scanner.nextLine();
        String[] idtSairam = scanner.nextLine().split(" ");      

        Queue<String> fila = new LinkedList<String>();
        for (int i = 0; i < qtdPessoasFila; i++) {
            fila.add(identificadores[i]);
        }

        for (int i = 0; i < qtd_sairam; i++) {
            fila.remove(idtSairam[i]);
        }
        int i = 0;
        for (String permaneceram: fila) {
           if (i == fila.size() - 1) {
            System.out.print(permaneceram);
           } else {
            System.out.print(permaneceram + " ");
           }
            i++;
        }
        System.out.print("\n");
        scanner.close();
    }
}
