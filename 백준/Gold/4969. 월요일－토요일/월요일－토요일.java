import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        while (true) {
            int num = input.nextInt();
            if (num == 1) break;
            else {
                System.out.print(num + ":");
                printFactor(num);
            }
        }
    }

    static void printFactor(int num) {
        boolean[] check = new boolean[num + 1];
        for (int i = 2; i <= num; i++) {
            if (num % i == 0 && check[i] == false && (i % 7 == 1 || i % 7 == 6)) {
                System.out.print(" " + i);
                for (int j = i * 2; j <= num; j += i) {
                    check[j] = true;
                }
            }
        }
        System.out.println();
    }
}
