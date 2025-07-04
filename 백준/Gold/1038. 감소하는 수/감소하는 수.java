import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        ArrayList<Long> decreasingNum = new ArrayList<>();

        for (int i = 1; i < 1024; i++) {
            String binaryNum = Integer.toBinaryString(i);
            if (binaryNum.length() < 10) {
                int length = binaryNum.length();
                for (int j = 0; j < 10 - length; j++) {
                    binaryNum = "0" + binaryNum;
                }
            }
            String strNum = "";
            for (int j = 9; j >= 0; j--) {
                if (binaryNum.charAt(j) == '1') {
                    strNum += String.valueOf(j);
                }
            }
            long tmpNum = 0;
            if (!strNum.equals("")) {
                tmpNum = Long.parseLong(strNum);
            }
            decreasingNum.add(tmpNum);
        }
        Collections.sort(decreasingNum);

        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        if (n < 1023) {
            System.out.println(decreasingNum.get(n));
        } else {
            System.out.println(-1);
        }
    }
}
