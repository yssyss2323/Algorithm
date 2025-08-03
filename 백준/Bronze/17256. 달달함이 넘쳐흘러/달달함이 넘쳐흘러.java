import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new  Scanner(System.in);
        int[] arr= new int[6];
        for (int i = 0; i < 6; i++) {
            arr[i]=input.nextInt();
        }
        int bx = arr[3] - arr[2];
        int by = arr[4] / arr[1];
        int bz = arr[5] - arr[0];

        System.out.println(bx + " " + by + " " + bz);
    }
}
