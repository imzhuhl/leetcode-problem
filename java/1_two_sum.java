/** 
    use hash table
    time complexity O(n), space complexity O(n)

    maybe another solution:
        1. sort the nums
        2. two pointers
 */

public static int[] twoSum(int[] nums, int target) {
    Map<Integer, Integer> map = new HashMap<>();
    for (int i = 0; i < nums.length; i++) {
        int tmp = target - nums[i];
        if (map.containsKey(tmp)) {
            return new int[]{map.get(tmp), i};
        }
        map.put(nums[i], i);
    }
    throw new IllegalArgumentException("no solution");
}