class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        result = [0] * n

        for i in range(n - 1, - 1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()

            if stack:
                result[i] = stack[-1] - i

            stack.append(i)



        return result
        

# class Solution:
    
#     #[73,72,71,74,69,72,76,73]
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         answer = [0] * len(temperatures)
#         stack = []
        
#         for i, temperature in enumerate(temperatures):
            
#             while stack and temperature > temperatures[stack[-1]]:
#                 prev_i = stack.pop()
#                 answer[prev_i] = i - prev_i
            
#             stack.append(i)
            
        
#         return answer