import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String a = input.next();
        String b = input.next();

        int ans = a.length();
        for (int i = 0; i < b.length() - a.length() + 1; i++) {
            int tmp = 0;
            for (int j = 0; j < a.length(); j++) {
                if (a.charAt(j) != b.charAt(i + j)) {
                    tmp++;
                }
            }
            if (tmp < ans) {
                ans = tmp;
            }
        }
        System.out.println(ans);
    }
}