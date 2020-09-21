#include <iostream>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};


class Solution {
    int sum = 0;
public:
    TreeNode* convertBST(TreeNode* root) {
        dfs(root);
        return root;
    }

    int dfs(TreeNode* node) {
        if (node == nullptr) {
            return 0;
        }
        dfs(node->right);
        sum += node->val;
        node->val = sum;
        dfs(node->left);
        return 0;
    }
};