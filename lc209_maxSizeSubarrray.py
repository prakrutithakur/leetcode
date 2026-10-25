# class Solution:
#     def minSubArrayLen(self, target: int, nums: list[int]) -> int:
#         l=0
#         r=0
#         n=len(nums)
#         current_sum=nums[l]
#         least_len=float('inf')
#         is_subarray_available=False
#         while r<n and l<=r:
#             len_subarray=r-l+1
#             if len_subarray<least_len and current_sum>=target:
#                 least_len=len_subarray
#                 is_subarray_available=True
#             if current_sum==target and r<n-1:
#                 l=r
#                 r+=1
#                 current_sum=nums[r]+nums[l]
#             elif current_sum>target:
#                 current_sum-=nums[l]
#                 l+=1
#             else:
#                 r+=1
#                 if r<n:
#                     current_sum+=nums[r]
#         if not is_subarray_available:
#             return 0
#         return least_len

#optimal solution
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        least_len = float('inf')
        current_sum = 0
        left = 0
        
        # Outer loop expands the window
        for right in range(n):
            current_sum += nums[right]
            
            # Inner loop contracts the window optimally
            while current_sum >= target:
                least_len = min(least_len, right - left + 1)
                current_sum -= nums[left]
                left += 1
                
        return 0 if least_len == float('inf') else least_len

if __name__=="__main__":
    sol=Solution()
    print(sol.minSubArrayLen(7,[2,3,1,2,4,3]))
    print(sol.minSubArrayLen(4,[1,4,4]))
    print(sol.minSubArrayLen(11,[1,1,1,1,1,1,1,1]))