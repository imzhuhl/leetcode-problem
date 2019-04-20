/**
    time: O(n)
    two pointers
 */

public static int maxArea(int[] height) {
    int left = 0, right = height.length - 1;
    int maxS = 0;
    while (left < right) {
        int h, tmp = (right - left);
        if (height[left] < height[right]) {
            h = height[left];
            left++;
        } else {
            h = height[right];
            right--;
        }
        tmp = tmp * h;
        if (maxS < tmp) maxS = tmp;
    }
    return maxS;
}