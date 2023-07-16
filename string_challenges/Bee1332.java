package string_challenges;

import java.util.Scanner;

public class Bee1332 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();

        for (int i = 0; i < n; i++) {
            String word = sc.nextLine();
            
            if (word.startsWith("o")) {
                System.out.println(1);
            } else if (word.startsWith("t") && word.length() == 3) {
                System.out.println(2);
            } else if (word.length() == 5){
                System.out.println(3);
            }
        }
        sc.close();

    }
}
