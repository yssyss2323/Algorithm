import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        for (int t = 0; t < 3; t++) {
            int[] startTime = new int[3];
            int[] endTime = new int[3];
            int[] ansTime = new int[3];

            for (int i = 0; i < 3; i++) {
                startTime[i] = input.nextInt();
            }
            for (int i = 0; i < 3; i++) {
                endTime[i] = input.nextInt();
            }

            ansTime[2] = endTime[2] - startTime[2];
            if (ansTime[2] < 0) {
                ansTime[2] += 60;
                endTime[1] -= 1;
            }

            ansTime[1] = endTime[1] - startTime[1];
            if (ansTime[1] < 0) {
                ansTime[1] += 60;
                endTime[0] -= 1;
            }

            ansTime[0] = endTime[0] - startTime[0];

            System.out.println(ansTime[0] + " " + ansTime[1] + " " + ansTime[2]);
        }
    }
}
