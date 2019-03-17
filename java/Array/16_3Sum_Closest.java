public static int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int minClose = 0x7fffffff;
        int rstSum = 0;
        for (int i = 0; i < nums.length - 2; i++) {
            // two pointers
            int left = i + 1, right = nums.length - 1;
            while (left < right) {
                int x = nums[i] + nums[left] + nums[right];
                int d = Math.abs(x - target);
                if (d < minClose) {
                    minClose = d;
                    rstSum = x;
                }
                if (x < target) {
                    left++;
                } else if (x > target) {
                    right--;
                } else {
                    break;
                }
            }
            if (minClose == 0) return rstSum;
        }
        return rstSum;
        