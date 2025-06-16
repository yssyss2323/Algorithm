import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        while (true) {
            String line = br.readLine();
            if (line == null || line.isEmpty()) continue;

            int num = Integer.parseInt(line);
            if (num == 1) break;

            sb.append(num).append(":");
            sb.append(printFactor(num)).append("\n");
        }

        System.out.print(sb);
    }

    static String printFactor(int num) {
        boolean[] check = new boolean[num + 1];
        StringBuilder sb = new StringBuilder();

        for (int i = 2; i <= num; i++) {
            if (num % i == 0 && !check[i] && (i % 7 == 1 || i % 7 == 6)) {
                sb.append(" ").append(i);
                for (int j = i * 2; j <= num; j += i) {
                    check[j] = true;
                }
            }
        }

        return sb.toString();
    }
}