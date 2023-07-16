package string_challenges;

import java.util.Scanner;

public class Bee1024 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();

        for (int i = 0; i < n; i++) {
            String string = sc.nextLine();
            String ans = halfDesloc(reverse(desloc3(string)));
            System.out.println(ans);
        }


        sc.close();
    }

    static String desloc3(String str) {
        char[] arr = str.toCharArray();
        StringBuilder ans = new StringBuilder();

        for (int i = 0; i < arr.length; i++) {
            char currentChar = arr[i];

            if (Character.isUpperCase(currentChar) || Character.isLowerCase(currentChar)) {
                ans.append((char) (currentChar + 3));
            } else {
                ans.append(currentChar);
            }
        }

        return ans.toString();
    }

    static String reverse(String str) {
        return new StringBuilder(str).reverse().toString();
    }

    static String halfDesloc(String str) {
        String substring = str.substring(0, str.length() / 2);
        char[] arr = str.toCharArray();
        StringBuilder ans = new StringBuilder();

        ans.append(substring);

        for (int i = arr.length / 2; i < arr.length; i++) {
            ans.append((char) (arr[i] - 1));
        } 

        return ans.toString();
    }

}
