import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int n = input.nextInt();
        System.out.print("3");
        for (int i = 1; i < n; i++) {
            System.out.print(" " + i * 6);
        }
    }
}
