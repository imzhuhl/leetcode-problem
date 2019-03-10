#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    string longestPalindrome(string s) {
        int left = 0, right = 0;
        int maxlen = 0;
        int dp[1001][1001];
        memset(dp, 0, sizeof(dp));
        for (int i = 0; i <= s.length(); i++) {
            dp[i][i] = 1;
        }
        for (int k = 2; k <= s.length(); k++) {
            for (int i = 0; i <= s.length() - k; i++) {
                if (s[i] == s[i+k-1] && (k == 2 || dp[i+1][i+k-2] == 1)) {
                    dp[i][i+k-1] = 1;
                    if (right - left + 1 < k) {
                        left = i;
                        right = i + k - 1;
                    }
                }
            }
        }
        return s.substr(left, right - left + 1);
    }
};

int main() {
    Solution so;
    string s = "babad";
    string rst = so.longestPalindrome(s);
    cout << rst << endl;

    return 0;
}