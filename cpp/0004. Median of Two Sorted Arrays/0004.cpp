#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int len1 = nums1.size(), len2 = nums2.size();
        int totalLen = len1 + len2;
        if (totalLen % 2 == 1) {
            return getKthElem(nums1, nums2, (totalLen+1) / 2);
        } else {
            return (
                getKthElem(nums1, nums2, totalLen / 2) + getKthElem(nums1, nums2, totalLen / 2 + 1)
            ) / 2;
        }
    }

    double getKthElem(vector<int>& nums1, vector<int>& nums2, int k) {
        int len1 = nums1.size();
        int len2 = nums2.size();
        int n1Left = 0, n2Left = 0;
        
        while (1) {
            if (n1Left == len1) {
                return nums2[n2Left + k - 1];
            } else if (n2Left == len2) {
                return nums1[n1Left + k - 1];
            } else if (k == 1) {
                return min(nums1[n1Left], nums2[n2Left]);
            }

            int idx1 = min(n1Left + k / 2 - 1, len1 - 1);
            int idx2 = min(n2Left + k / 2 - 1, len2 - 1);

            if (nums1[idx1] <= nums2[idx2]) {
                k = k - (idx1 - n1Left + 1);
                n1Left = idx1 + 1;
            } else {
                k = k - (idx2 - n2Left + 1);
                n2Left = idx2 + 1;
            }
        }

    }

};