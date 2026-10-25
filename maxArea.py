from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea=0
        l=0
        r=len(height)-1
        while(l<r):
            current_height=min(height[l],height[r])
            current_area=(r-l)*current_height
            if(current_area>maxArea):
                maxArea=current_area
            if(height[l]>height[r]):
                r-=1
            else:
                l+=1
        return maxArea

if __name__ == "__main__":
    sol=Solution()
    height=[int(x) for x in input("Enter numbers separated by spaces: ").split(",")]
    print("height array,",height)
    print(sol.maxArea(height))