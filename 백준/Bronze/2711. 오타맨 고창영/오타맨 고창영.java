import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int t = input.nextInt();
        for (int i = 0; i < t; i++) {
            int idx =  input.nextInt();
            String str = input.next();
            for (int j = 0; j < str.length(); j++) {
                if (j != idx - 1) {
                    System.out.print(str.charAt(j));
                }
            }
            System.out.println();
        }
    }
}