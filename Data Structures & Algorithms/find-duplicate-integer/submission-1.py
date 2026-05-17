class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        #Phase 1 find intersection point of the two pointers
        #(Floyd's cycle detection algorithm)
        tortoise = nums[0]
        hare = nums[0]
        while True:
            tortoise = nums[tortoise] # move 1 step
            hare = nums[nums[hare]] # move 2 step
            if tortoise == hare:
                break
        

        #Phase2 find the enterance of the cycle (the duplicate)
        finder = nums[0]
        while tortoise != finder:
            tortoise = nums[tortoise] #both move 1 step
            finder = nums[finder]
            if tortoise == finder:
                break
        return tortoise