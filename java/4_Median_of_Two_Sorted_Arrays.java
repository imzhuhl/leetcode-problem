/**
    time complexity O(m + n)
 */
public static double findMedianSortedArrays(int[] nums1, int[] nums2) {
    int totalLen = nums1.length + nums2.length;
    int firstIdx = (totalLen - 1) / 2;
    int idx1 = 0, idx2 = 0, cnt = 0;
    int[] nums = {0, 0};
    // remove the small half
    while (idx1 < nums1.length && idx2 < nums2.length && cnt < firstIdx) {
        if (nums1[idx1] < nums2[idx2]) {
            idx1++;
            cnt++;
        } else {
            idx2++;
            cnt++;
        }
    }
    // if one array is "empty" but we don't remove small half completely
    while (cnt < firstIdx && idx1 < nums1.length) {
        idx1++;
        cnt++;
    }
    while (cnt < firstIdx && idx2 < nums2.length) {
        idx2++;
        cnt++;
    }

    // put first mid number into nums[0]
    if (idx1 >= nums1.length) {
        nums[0] = nums2[idx2++];
    } else if (idx2 >= nums2.length) {
        nums[0] = nums1[idx1++];
    } else {
        nums[0] = nums1[idx1] < nums2[idx2] ? nums1[idx1++] : nums2[idx2++];
    }

    // if totalLen is odd, return first mid number immediately
    if (totalLen % 2 == 1) {
        return nums[0] * 1.0;
    }

    // if totalLen is even, we need next number, put into nums[1]
    if (idx1 >= nums1.length) {
        nums[1] = nums2[idx2++];
    } else if (idx2 >= nums2.length) {
        nums[1] = nums1[idx1++];
    } else {
        nums[1] = nums1[idx1] < nums2[idx2] ? nums1[idx1++] : nums2[idx2++];
    }
    return (nums[0] + nums[1]) * 1.0 / 2;

}