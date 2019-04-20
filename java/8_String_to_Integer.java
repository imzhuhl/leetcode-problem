public static int myAtoi(String str) {
    int idx = 0, rst = 0;
    boolean flag = false;

    while (idx < str.length() && str.charAt(idx) == ' ') {
        idx++;
    }
    if (idx >= str.length()) return 0;
    if (str.charAt(idx) == '+') {
        idx++;
    } else if (str.charAt(idx) == '-') {
        flag = true;
        idx++;
    }
    if (idx >= str.length()) return 0;
    if (Character.isDigit(str.charAt(idx))) {
        while (idx < str.length() && Character.isDigit(str.charAt(idx))) {
            int dig = str.charAt(idx) - '0';
            if (rst > Integer.MAX_VALUE / 10
                    || (rst == Integer.MAX_VALUE / 10 && dig > 7)) {
                if (flag) return Integer.MIN_VALUE;
                else return Integer.MAX_VALUE;
            }
            rst *= 10;
            rst += dig;
            idx++;
        }
        if (flag) rst = -rst;
        return rst;
    } else {
        return 0;
    }
}