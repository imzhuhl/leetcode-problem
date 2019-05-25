// 溢出就返回 0
public int reverse(int x) {
    int rst = 0;
    int digit;
    while (x != 0) {
        digit = x % 10;
        x /= 10;
        if (rst > Integer.MAX_VALUE / 10 || (rst == Integer.MAX_VALUE / 10 && digit > 7)) {
            return 0;
        }
        if (rst < Integer.MIN_VALUE / 10 || (rst == Integer.MIN_VALUE / 10 && digit < -8)) {
            return 0;
        }

        rst = rst * 10 + digit;
    }
    return rst;
}