import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        int lambda = input.nextInt();

        String ans;
        if (lambda >= 620) ans = "Red";
        else if (lambda >= 590) ans = "Orange";
        else if (lambda >= 570) ans = "Yellow";
        else if (lambda >= 495) ans = "Green";
        else if (lambda >= 450) ans = "Blue";
        else if (lambda >= 425) ans = "Indigo";
        else ans = "Violet";

        System.out.println(ans);
    }
}
