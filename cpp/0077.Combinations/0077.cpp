#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<int> path;
        vector<vector<int>> rst;

        dfs(1, n, k, path, rst);

        return rst;
    }

    void dfs(int cur, int n, int k, vector<int>& path, vector<vector<int>>& rst) {
        if (path.size() + (n-cur+1) < k) {
            return;
        }

        if (path.size() == k) {
            rst.push_back(path);
            return;
        }

        path.push_back(cur);
        dfs(cur+1, n, k, path, rst);
        path.pop_back();

        dfs(cur+1, n, k, path, rst);

    }

};


int main() {

    cout << "============= Test ==============" << endl;
    
    Solution solu;
    auto rst = solu.combine(4, 2);

    
    return 0;
}

