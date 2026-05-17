class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        seq_headers = []

        for num in nums:
            if num - 1 not in nums_set:
                seq_headers.append(num)

        seq_lengths = []
        for header in seq_headers:
            seq = 1
            while True:
                if header + 1 in nums_set:
                    seq += 1
                    header += 1
                else:
                    seq_lengths.append(seq)
                    break;
        
        if len(seq_lengths) == 0:
            return 0

        return max(seq_lengths)
        