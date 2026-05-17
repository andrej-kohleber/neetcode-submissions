class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
     
        result = []
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    result.append(i + 1)
                    result.append(j + 1)
                    break
                if numbers[i] + numbers[j] > target:
                    continue
              
        return result
        