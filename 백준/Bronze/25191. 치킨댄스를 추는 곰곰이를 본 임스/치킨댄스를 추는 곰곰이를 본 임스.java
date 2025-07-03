import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int ans = input.nextInt();
        int a = input.nextInt();
        int b = input.nextInt();
        int tmp = a / 2 + b;
        if (tmp < ans) ans = tmp;
        System.out.println(ans);;
    }
}
