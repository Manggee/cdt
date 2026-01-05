package Lv0;

public class Q3 {
    public String solution(String my_string, String alp) {
        char target = alp.charAt(0); // target 설정
        StringBuilder sb = new StringBuilder(); // StringBuilder는 무엇이며 왜 사용할까?

        for (int i = 0; i < my_string.length(); i++) {
            char ch = my_string.charAt(i);
            if (ch == target) {
                sb.append(Character.toUpperCase(ch));
            } else {
                sb.append(ch);
            }
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        Q3 s = new Q3();
        System.out.println(s.solution("programmers", "p"));
    }
}