/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
int counter,target;
int ans;

void rec(TreeNode *A)
{
    if(A == nullptr || ans < INT_MAX) return;
    rec(A->left);
    counter++;
    if(counter == target) {
        ans = A->val;
        return;
    }
    rec(A->right);

    return;
}
class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        counter = 0; target = k;
        ans = INT_MAX;
        rec(root);
        return ans;
    }
};
