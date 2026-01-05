package Lv0;

public class Q3 {
    public int solution(int[] args) {
        for (int i = 0; i < args.length; i++) {
            if (args[i] < 0) {
                return i;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        Q3 s = new Q3();

        int[] a = {12, 4, 15, 46, 38, -2, 15};
        int[] b = {13, 22, 53, 24, 15, 6};

        System.out.println(s.solution(a));
        System.out.println(s.solution(b));
    }
}
