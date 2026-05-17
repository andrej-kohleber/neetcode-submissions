class Solution {

    // 3 4 5 6  -- 7
    // 

    public int[] twoSum(int[] nums, int target) {
        int[] answer = {0, 0};
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int diff = target - nums[i];
            if (map.containsKey(diff)) {
                answer[0] = map.get(diff);
                answer[1] = i;
            } else {
                 map.put(nums[i], i);
            }
           
        }
        return answer;
    }
}
