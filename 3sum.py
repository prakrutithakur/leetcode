class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans=[]
        nums.sort()
        i=0
        while i<len(nums)-2:
            j=i+1
            k=len(nums)-1
            while j<k:
                sum_indices=nums[i]+nums[j]+nums[k]
                if sum_indices==0:
                    ans.append([nums[i],nums[j],nums[k]])
                    while nums[k-1]==nums[k]:
                        k-=1
                    k-=1
                    while j<k and nums[j+1]==nums[j] :
                        j+=1
                    j+=1
                elif sum_indices>0:
                    while j<k and nums[k-1]==nums[k]:
                        k-=1
                    k-=1
                else:
                    while j<k and nums[j+1]==nums[j]:
                        j+=1
                    j+=1
            while nums[i+1]==nums[i] and i<len(nums)-2:
                i+=1
            i+=1
        return ans


if __name__=="__main__":
    sol=Solution()
    # nums=[-1,0,1,2,-1,-4]
    nums=[-2,-3,0,0,-2]
    print(sol.threeSum(nums))
