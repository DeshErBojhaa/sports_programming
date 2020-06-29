// 137. Single Number II
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int x1 = 0, x2 = 0, mask = 0;
        for(int n: nums) {
            x2 ^= (x1 & n);
            x1 ^= n;
            mask = ~(x1 & x2);
            x1 &= mask;
            x2 &= mask;
        }
        return x1;
    }
};
