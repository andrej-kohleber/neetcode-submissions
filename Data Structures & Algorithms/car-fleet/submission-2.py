class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        

        cars = []
        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            cars.append((position[i], time))

        cars.sort(reverse=True)

        fleetCnt = 0
        maxTime = 0

        for pos, time in cars:
            if time > maxTime:
                maxTime = time
                fleetCnt += 1



        return fleetCnt



