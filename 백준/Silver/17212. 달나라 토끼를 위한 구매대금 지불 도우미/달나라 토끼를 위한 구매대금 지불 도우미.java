import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int[] mod7 = {0, 1, 1, 2, 2, 1, 2, 1};
        int n = input.nextInt();
        if (n <= 7) {
            System.out.println(mod7[n]);
        } else{
            int[] arr = new int[n + 1];
            for (int i = 0; i < 7; i++) {
                arr[i] = mod7[i];
            }
            for (int i = 7; i <= n; i++) {
                arr[i] = arr[i - 5] < arr[i - 7] ? arr[i - 5] + 1 : arr[i - 7] + 1;
            }
            System.out.println(arr[n]);
        }
    }
}