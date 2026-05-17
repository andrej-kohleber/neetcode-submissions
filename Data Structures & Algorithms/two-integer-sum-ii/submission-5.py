class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
     
        result = []
        i = 0
        j = len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] == target:
                result.append(i + 1)
                result.append(j + 1)
                break
            if numbers[i] + numbers[j] > target:
                j -= 1
                continue
            if numbers[i] + numbers[j] < target:
                i += 1
                continue

              
        return result
        