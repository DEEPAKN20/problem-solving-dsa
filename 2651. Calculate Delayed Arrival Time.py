#https://leetcode.com/problems/calculate-delayed-arrival-time/description/
#https://leetcode.com/submissions/detail/2146587592/ - Solution 1
#https://leetcode.com/problems/calculate-delayed-arrival-time/submissions/2146606245/ - Solution 2

#19 September 2026 - 5 Mins

# Solution 1
class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        return (arrivalTime+delayedTime)%24

# Solution 2
class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        sum= arrivalTime + delayedTime
        if sum>=24:
            sum-=24
        return sum
"""

"""
        
        