from typing import List
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        track_counts=defaultdict(int)
        possible_counts=defaultdict(list)
        max_count=0

        for i in nums:
            track_counts[i]+=1
            possible_counts[track_counts[i]].append(i)
            if track_counts[i]>max_count:
                max_count=track_counts[i]

        most_frequent=[]
        for i in range(max_count,-1,-1):
            if i in possible_counts:
                most_frequent.extend(possible_counts[i])
                if len(set(most_frequent))==k:
                    return list(set(most_frequent))

if __name__=="__main__":
    sol=Solution()
    print(sol.topKFrequent([1,1,1,2,2,3],2))
    print(sol.topKFrequent([1],1))
    print(sol.topKFrequent([1,2,1,2,1,2,3,1,3,2],2))
    print(sol.topKFrequent([1, 1, 2, 2, 2],1))
    print(sol.topKFrequent([1, 1, 2, 3],1))
    print(sol.topKFrequent([1, 2, 3, 4],2))

            

            
