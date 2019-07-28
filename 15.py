import java.lang.System;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> triplets = new ArrayList<>();
        int len = nums.length;
        Arrays.sort(nums);
        for (int i = 0; i < len - 2; i++) {
            if (i > 0)
                while (i < len - 2 && nums[i - 1] == nums[i])
                    i++; // to exclude duplicates
            int j = i + 1;
            int k = len - 1;
            while (j < k) {
                int sum = nums[i] + nums[j] + nums[k];
                if (sum == 0) {
                    triplets.add(new ArrayList<>(Arrays.asList(nums[i], nums[j], nums[k])));
                    j++;
                    k--;
                    while ((j < k) && (nums[j - 1] == nums[j])) // to exclude duplicates
                        j++;
                    while ((j < k) && (nums[k] == nums[k + 1])) // to exclude duplicates
                        k--;
                } else if (sum < 0) {
                    j++; // sum too low
                } else {
                    k--; // sum too high
                }
            }
        }
        return triplets; 
    }
}
