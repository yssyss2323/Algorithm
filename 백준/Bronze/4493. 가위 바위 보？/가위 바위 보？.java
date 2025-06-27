import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        int t = input.nextInt();
        for (int i = 0; i < t; i++) {
            int winPlayer1 = 0;
            int winPlayer2 = 0;

            int n = input.nextInt();
            for (int j = 0; j < n; j++) {
                String player1 = input.next();
                String player2 = input.next();

                if (player1.equals(player2)) continue;
                if (player1.equals("R")) {
                    if (player2.equals("S")) {
                        winPlayer1++;
                    } else {
                        winPlayer2++;
                    }
                } else if (player1.equals("S")) {
                    if (player2.equals("P")) {
                        winPlayer1++;
                    } else {
                        winPlayer2++;
                    }
                } else {
                    if (player2.equals("R")) {
                        winPlayer1++;
                    } else {
                        winPlayer2++;
                    }
                }
            }
            
            if (winPlayer1 > winPlayer2) {
                System.out.println("Player 1");
            } else if (winPlayer1 < winPlayer2) {
                System.out.println("Player 2");
            } else {
                System.out.println("TIE");
            }
        }
    }
}
