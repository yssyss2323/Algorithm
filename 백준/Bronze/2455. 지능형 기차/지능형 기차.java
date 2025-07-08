import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int ans = 0;
        int tot = 0;

        for (int i = 0; i < 4; i++) {
            int out = input.nextInt();
            int in = input.nextInt();
            tot += in - out;
            if (tot > ans) ans = tot;
        }

        System.out.println(ans);
        
    }
}