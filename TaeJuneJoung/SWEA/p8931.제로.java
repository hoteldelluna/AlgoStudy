import java.util.Scanner;
import java.io.FileInputStream;

class Solution
{
    public static void main(String args[]) throws Exception
    {
        Scanner sc = new Scanner(System.in);
        int T;
        T=sc.nextInt();

        for(int test_case = 1; test_case <= T; test_case++)
        {
            int K = sc.nextInt();
            int[] nums = new int[K];
            int idx = 0;
            int value = 0;
            for(int i=0; i < K; i++) {
                value = sc.nextInt();
                if(value > 0) {
                    nums[idx] = value;
                    idx++;
                } else {
                    idx--;
                    nums[idx] = 0;
                }
            }

            long sumV = 0;
            for(int i=0; i < nums.length; i++) {
                if(nums[i] > 0) {
                    sumV += nums[i];
                } else {
                    break;
                }
            }

            System.out.println("#" + test_case + " " + sumV);
        }
    }
}