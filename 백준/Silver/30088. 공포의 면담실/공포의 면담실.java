import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        long[] arr = new long[n];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int cnt = Integer.parseInt(st.nextToken());
            long sum = 0;
            for (int j = 0; j < cnt; j++) {
                sum += Long.parseLong(st.nextToken());
            }
            arr[i] = sum;
        }

        Arrays.sort(arr);

        long ans = 0;
        long tmp = 0;
        for (int i = 0; i < n; i++) {
            tmp += arr[i];
            ans += tmp;
        }

        System.out.println(ans);
    }
}
