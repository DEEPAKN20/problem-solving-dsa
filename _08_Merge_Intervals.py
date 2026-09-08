#https://leetcode.com/problems/merge-intervals/description/?envType=problem-list-v2&envId=array
#https://leetcode.com/problems/merge-intervals/submissions/2126144672/

#31 August 2026-30 mins

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result=[]
        start=intervals[0][0]
        end=intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0]<=end:
                end=max(end,intervals[i][1])
            else:
                result.append([start,end])

                start=intervals[i][0]
                end=intervals[i][1]
        result.append([start,end])
        return result

    """
    quick sort
    
    """



        
        