import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int A = scanner.nextInt();
        int M = scanner.nextInt();
        int B = (2 * M) - A;

        System.out.println(B);
        scanner.close();
    }
}