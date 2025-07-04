import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int n = input.nextInt();
        int m = input.nextInt();

        boolean flag = false;
        int x1 = 0, y1 = 0, x2 = 0, y2 = 0;
        int[][] arr = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                arr[i][j] = input.nextInt();
                if (arr[i][j] == 1) {
                    if (!flag) {
                        x1 = i;
                        y1 = j;
                        flag = true;
                    } else {
                        x2 = i;
                        y2 = j;
                    }
                }
            }
        }
        int ans = Math.abs(x1 - x2) + Math.abs(y1 - y2);
        System.out.println(ans);
    }
}