import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        int a = input.nextInt();
        int b = input.nextInt();

        int check = 1;
        int minSum = 0, maxSum = 0;

        while (a > 0 || b > 0) {
            int tmpa = a % 10;
            int tmpb = b % 10;
            a /= 10;
            b /= 10;

            if (tmpa == 5 || tmpa == 6) {
                if (tmpb == 5 || tmpb == 6) {
                    minSum += 10 * check;
                    maxSum += 12 * check;
                } else {
                    minSum += (tmpb + 5) * check;
                    maxSum += (tmpb + 6) * check;
                }
            } else if (tmpb == 5 || tmpb == 6){
                minSum += (tmpa + 5) * check;
                maxSum += (tmpa + 6) * check;
            } else {
                minSum += (tmpa + tmpb) * check;
                maxSum += (tmpa + tmpb) * check;
            }
            check *= 10;
        }
        System.out.println(minSum + " " + maxSum);
    }
}
