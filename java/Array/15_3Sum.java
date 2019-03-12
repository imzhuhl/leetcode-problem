/**
    time: O(n^2)
 */
public static List<List<Integer>> threeSum(int[] nums) {
    Arrays.sort(nums);
    List<List<Integer>> rst = new ArrayList<>();
    for (int i = 0; i < nums.length - 2; i++) {
        if (nums[i] > 0) break;
        if (i != 0 && nums[i] == nums[i - 1]) continue;

        // two pointers
        int left = i + 1, right = nums.length - 1, target = 0 - nums[i];
        while (left < right) {
            if (left != i + 1 && nums[left] == nums[left - 1]) {
                left++;
                continue;
            }
            if (right != nums.length - 1 && nums[right] == nums[right + 1]) {
                right--;
                continue;
            }
            int s = nums[left] + nums[right];
            if (target == s) {
                rst.add(Arrays.asList(nums[i], nums[left], nums[right]));
                left++;
                right--;
            } else if (target > s) {
                left++;
            } else {
                right--;
            }
        }
    }
    return rst;
}