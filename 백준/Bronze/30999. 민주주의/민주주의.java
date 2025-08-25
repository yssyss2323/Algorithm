import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int ans = 0;
        for (int i = 0; i < n; i++) {
            String curr = sc.next();
            int cnt = 0;
            for (int j = 0; j < m; j++) {
                if (curr.charAt(j) == 'O') {
                    cnt++;
                }
            }
            if (cnt * 2 > m) {
                ans++;
            }
        }
        System.out.println(ans);
    }
}