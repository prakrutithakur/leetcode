class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        closest_sum=abs(target-nums[0]+nums[1]+nums[2])
        ans=nums[0]+nums[1]+nums[2]
        k=len(nums)-1
        for i in range(len(nums)-2):
            j=i+1
            k=len(nums)-1
            if i>0 and nums[i-1]==nums[i]:
                continue
            while j<k:
                sum_of_nums=nums[i]+nums[j]+nums[k]
                target_sum_diff=abs(sum_of_nums-target)
                if(target_sum_diff==0):
                    return sum_of_nums
                if(closest_sum>target_sum_diff):
                    closest_sum=target_sum_diff
                    ans=sum_of_nums
                if(sum_of_nums>target):
                    k-=1
                    while j<k-1 and nums[k-1]==nums[k]:
                        k-=1
                else:
                    j+=1
                    while j-1<k and (nums[j-1]==nums[j]):
                        j+=1

        return ans

                    



if __name__=="__main__":
    sol=Solution()
    nums=[1,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,15,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,29]
    # nums=[-1,2,1,-4]
    # nums=[-4,2,2,3,3,3]
    target=45
    print(sol.threeSumClosest(nums, target))