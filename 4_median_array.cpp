#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

/**
 * 这题需要好好想一想，题目要求时间在 O(log(m + n))....
 */

class Solution {
public:
    double findMedianSortedArrays2(vector<int>& nums1, vector<int>& nums2) {
        int median;
        vector<int> rst;
        rst.insert(rst.end(), nums1.begin(), nums1.end());
        rst.insert(rst.end(), nums2.begin(), nums2.end());
        sort(rst.begin(), rst.end());
        int len = rst.size();
        int half = (len - 1) / 2;
        if (len % 2 == 1) {
            return rst[half] * 1.0;
        } else {
            return (rst[half] + rst[half + 1]) / 2.0;
        }
        
    }
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int m, n;
        vector<int> &A = nums1, &B = nums2;
        m = nums1.size();
        n = nums2.size();
        if (m > n) {
            return findMedianSortedArrays(nums2, nums1);
        }
        int left = 0, right = m, half_len = (m + n + 1) / 2;
        int i, j;
        int maxleft, minright;
        while (left <= right) {
            i = (left + right) / 2;
            j = half_len - i;
            if (i < m && B[j - 1] > A[i]) {
                left = i + 1;
            } else if (i > 0 && A[i - 1] > B[j]) {
                right = i - 1;
            } else {
                if (i == 0) maxleft = B[j - 1];
                else if (j == 0) maxleft = A[i - 1];
                else maxleft = max(A[i - 1], B[j - 1]);

                if ((m + n) % 2 == 1) {
                    return maxleft;
                }

                if (i == m) minright = B[j];
                else if (j == n) minright = A[i];
                else minright = min(A[i], B[j]);

                return (maxleft + minright) / 2.0;
            }
        }
    }
};

int main() {
    return 0;
}