class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            numOfDays = 0
            for j in range(i + 1, len(temperatures)):
                numOfDays += 1
                if temperatures[j] > temperatures[i]:
                    result[i] = numOfDays
                    break
                

        return result
        