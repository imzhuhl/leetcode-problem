#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        int type[3] = {0};
        for (int i = 0; i < bills.size(); i++) {
            if (bills[i] == 5) {
                type[0]++;
            } else if (bills[i] == 10) {
                type[0]--;
                type[1]++;
                if (type[0] < 0) {
                    return false;
                }
            } else {
                type[2]++;
                if (type[1] > 0) {
                    type[1]--;
                    type[0]--;
                } else {
                    type[0] -= 3;
                }
                if (type[0] < 0) {
                    return false;
                }
            }

        }
        return true;
    }
};


int main() {
    int a[] = {5,5,10,10,20};
    vector<int> r(a, a + 5);
    Solution so;
    so.lemonadeChange(r);
    return 0;
}