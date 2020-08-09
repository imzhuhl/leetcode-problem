#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1;
        if (nums.size() == 0) {
            return -1;
        }

        return searchA(nums, left, right, target);


    }

    int searchA(vector<int>& nums, int left, int right, int target) {
        int mid = (left + right) / 2;
        if (target == nums[mid]) {
            return mid;
        }

        if (left >= right) {
            return -1;
        }

        // 必定有一侧有序
        if (nums[left] <= nums[mid]) {
            if ((target >= nums[left]) && (target <= nums[mid])) {
                return searchA(nums, left, mid-1, target);
            } else {
                return searchA(nums, mid+1, right, target);
            }
        } else {  // nums[mid] < nums[right]
            if ((target >= nums[mid]) && (target <= nums[right])) {
                return searchA(nums, mid+1, right, target);
            } else {
                return searchA(nums, left, mid-1, target);
            }
        }

    }

};

int main() {
    auto nums = vector<int>{3, 1};
    int target = 1;
    auto solution = Solution();
    int rst = solution.search(nums, target);
    printf("%d\n", rst);
    return 0;
}