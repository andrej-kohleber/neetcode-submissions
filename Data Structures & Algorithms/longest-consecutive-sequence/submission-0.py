class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return 1;

        sequences = []
        nums.sort()

        seq_count = 1
        for i in range(1, length):
            diff = nums[i] - nums[i - 1]
            if diff == 1:
                seq_count += 1
            elif diff == 0:
                continue
            else:
                sequences.append(seq_count)
                seq_count = 1
        
        sequences.append(seq_count)
        sequences.sort()
     
        return sequences[-1]
        