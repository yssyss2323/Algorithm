import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        int[][] board = new int[8][8];
        Scanner sc = new Scanner(System.in);
        int ans = 0;
        for (int i = 0; i < 8; i++) {
            String tmp = sc.nextLine();
            for  (int j = 0; j < 8; j++) {
                board[i][j] = tmp.charAt(j);
                if ((i + j) % 2 == 0 && board[i][j] == 'F') {
                    ans++;
                }
            }
        }
        System.out.println(ans);
    }
}
