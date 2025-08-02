import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new  Scanner(System.in);
        String num =  input.nextLine();
        int ans = 0;
        for (int i = 0; i < num.length(); i++) {
            int currNum = num.charAt(i) - '0';
            ans += Math.pow(currNum, 5);
        }
        System.out.println(ans);
    }
}
