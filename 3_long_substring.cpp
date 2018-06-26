#include <iostream>
#include <string>
#include <set>
#include <unordered_set>
#include <deque>
#include <vector>
#include <algorithm>
using namespace std;


class Solution {
public:
    // fast 36ms
    int lengthOfLongestSubstring2(string s) {
        int longest = 0, start = 0;
        int flag[300];
        fill(flag, flag + 300, -1);
        for (int i = 0; i < s.size(); i++) {
            if (flag[s[i]] != -1) {
                if (start > flag[s[i]]) {
                    flag[s[i]] = i;
                } else {
                    start = flag[s[i]] + 1;
                    flag[s[i]] = i;
                }   
            } else {
                flag[s[i]] = i;
            }

            if (longest < i - start + 1) {
                longest = i - start + 1;
            }
        }
        return longest;
    }

    int lengthOfLongestSubstring(string s) {
        set<char> info;
        deque<char> rst;
        int longest = 0;
        char c;
        for (int i = 0; i < s.size(); i++) {
            if (info.find(s[i]) == info.end()) {
                info.insert(s[i]);
                rst.push_back(s[i]);
            } else {
                int len = rst.size();
                for (int j = 0; j < len; j++) {
                    if (rst.front() == s[i]) {
                        break;
                    }
                    info.erase(rst.front());
                    rst.pop_front();
                }
                rst.pop_front();
                rst.push_back(s[i]);
            }
            if (longest < rst.size()) {
                longest = rst.size();
            }
        }
        
        return longest;
    }
};

int main() {
    printf("%d\n", 'a');
    return 0;
}