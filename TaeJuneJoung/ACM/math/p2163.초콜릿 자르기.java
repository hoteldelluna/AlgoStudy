import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = Integer.parseInt(sc.nextLine().trim());
        System.out.println(M*N-1);
        sc.close();
    }
}