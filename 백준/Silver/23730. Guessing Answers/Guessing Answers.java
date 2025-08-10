import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] standard = new int[n + 2];
        standard[0] = -1;
        standard[n + 1] = -1;
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            standard[i + 1] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            int correctIndex = Integer.parseInt(st.nextToken());
            standard[correctIndex] *= -1;
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= n; i++) {
            int val = 0;
            if (standard[i] < 0) {
                standard[i] *= -1;
                val = standard[i];
            } else {
                for (int j = 1; j <= 5; j++) {
                    if (j != standard[i - 1] && j != standard[i] && j != Math.abs(standard[i + 1])) {
                        val = j;
                        standard[i] = j;
                        break;
                    }
                }
            }
            if (i == 1) {
                sb.append(val);
            } else {
                sb.append(" ").append(val);
            }
        }
        System.out.println(sb.toString());
    }
}