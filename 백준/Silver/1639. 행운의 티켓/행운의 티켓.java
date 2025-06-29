import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        String ticketNum = input.nextLine();
        char[] arr = ticketNum.toCharArray();
        int[] numArr = new int[ticketNum.length()];

        for (int i = 0; i < ticketNum.length(); i++) {
            numArr[i] = arr[i] - '0';
        }

        int ans = solv(numArr);

        System.out.println(ans);

    }

    public static int solv(int[] arr) {
        for (int i = (arr.length / 2) * 2; i >= 2; i -= 2) {
            for (int j = 0; j + i <= arr.length; j++) {
                int sum = 0;
                for (int k = 0; k < i / 2; k++) {
                    sum += arr[j + k] - arr[j + k + i / 2];
                }
                if (sum == 0) {
                    return i;
                }
            }
        }
        return 0;
    }
}
