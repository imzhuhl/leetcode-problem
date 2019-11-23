#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int minDistance(string word1, string word2){
    int row = word1.size(), col = word2.size();
    vector<vector<int>> dp(row+1, vector<int>(col+1));
    for (int i = 0; i <= row; ++i) {
        for (int j = 0; j <= col; ++j) {
            if (i == 0) {
                dp[i][j] = j;
                continue;
            }
            if (j == 0) {
                dp[i][j] = i;
                continue;
            }
            

        }
    }
    return 0;
}

int main(){
    string w1 = "horse";
    string w2 = "ros";
    minDistance(w1, w2);
    return 0;
}
