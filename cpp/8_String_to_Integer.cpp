#include <iostream>
#include <string>
#include <climits>
using namespace std;

class Solution {
  public:
    int myAtoi(string str) {
        int idx = 0, rst = 0;
        bool flag = false;

        while (idx < str.size() && str[idx] == ' ') {
            idx++;
        }
        if (idx >= str.length()) return 0;
        if (str[idx] == '+') {
            idx++;
        } else if (str[idx] == '-') {
            flag = true;
            idx++;
        }
        if (idx >= str.length()) return 0;
        if (isdigit(str[idx])) {
            while (idx < str.length() && isdigit(str[idx])) {
                int dig = str[idx] - '0';
                if (rst > INT_MAX / 10
                        || (rst == INT_MAX / 10 && dig > 7)) {
                    if (flag) return INT_MIN;
                    else return INT_MAX;
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
};

int main() { 
    Solution s;
    int a = s.myAtoi("4193 with words");
    printf("%d\n", a);
    return 0; 
}