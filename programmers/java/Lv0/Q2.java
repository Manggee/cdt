package Lv0;

public class Q2 {
    public int solution(int num, int n) {
        if (num % n == 0) {
            return 1;
        }
        else {
            return 0;
        }
    }

    public static void main(String[] args) {
        Q2 s = new Q2();
        System.out.println(s.solution(98, 2));
        System.out.println(s.solution(34, 3));
    }
}