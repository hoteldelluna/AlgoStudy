"""
Java Method를 공부하면서 재귀함수 공부할겸 풀어봄.
1. 백준 Java의 클래스 이름은 Main이어야하나봄(?)
    이를 몰라 많은 '컴파일 에러'를 만남

2. 틀렸습니다 -> N이 100이므로 타입 범위 초과
    int는 2^31-1까지고 long은 2^63-1까지인데
    2^100이 되는 값이 필요
    이를 해결하기 위해 `BigInteger`을 사용
"""

import java.math.BigInteger;
import java.util.Scanner;

public class Main {
    static void hanoi(int disk, char from, char mid, char to) {
        if(disk == 1) {
            System.out.println( from + " " + to);
            return;
        } else {
            hanoi(disk-1, from, to, mid);
            System.out.println( from + " " + to);
            hanoi(disk-1, mid, from, to);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int disk = sc.nextInt();
        BigInteger bigInt = new BigInteger("2");
        System.out.println(bigInt.pow(disk).subtract(BigInteger.ONE));
        if(disk <= 20) {
            hanoi(disk, '1', '2', '3');
        }
    }
}