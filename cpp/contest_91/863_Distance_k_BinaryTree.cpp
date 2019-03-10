#include <iostream>
#include <vector>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    void dfs(TreeNode *p) {
        if (p == NULL) return;
        if (p->val == target_val) {
            flag = 1;
            return;
        }
        node.push_back(p);
        dfs(p->left);
        if (flag == 1) return;
        dfs(p->right);
        if (flag == 1) return;
        node.pop_back();
    }
    vector<int> distanceK(TreeNode* root, TreeNode* target, int K) {
        target_val = target->val;
    }
private:
    int flag = 0;
    int target_val = -1;
    vector<TreeNode*> node;

};