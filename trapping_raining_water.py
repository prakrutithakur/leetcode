# class Solution:

#     def remove_trailing_zeros(self, height, length)-> list[int]:
#         left=0
#         right=length-1
#         while left<right:
#             if height[left]==0:
#                 left+=1
#             if height[right]==0:
#                 right-=1
#             if height[left]!=0 and height[right]!=0:
#                 break
#         return height[left:right+1]
    
#     def trap(self, height: list[int]) -> int:
#         ans=0
#         updated_height=self.remove_trailing_zeros(height, len(height))
#         highest_left_index=0
#         new_length=len(updated_height)
#         accumulated_height=0
#         for i in range(new_length):
#             if(updated_height[highest_left_index]<=updated_height[i] and i!=highest_left_index):
#                 ans+=(updated_height[highest_left_index]*(i-highest_left_index-1))-accumulated_height
#                 highest_left_index=i
#                 accumulated_height=0
#             else:
#                 if i!=highest_left_index:
#                     accumulated_height+=updated_height[i]
#         if accumulated_height>0:
#             accumulated_height=0
#             highest_right_index=new_length-1
#             for i in range(new_length-1,highest_left_index-1,-1):
#                         if(updated_height[highest_right_index]<=updated_height[i] and i!=highest_right_index):
#                             ans+=(updated_height[highest_right_index]*(highest_right_index-i-1))-accumulated_height
#                             highest_right_index=i
#                             accumulated_height=0
#                         else:
#                             if i!=highest_right_index:
#                                 accumulated_height+=updated_height[i]
#         return ans


# gemini solution
# class Solution:
#     def trap(self, height: list[int]) -> int:
#         if not height:
#             return 0
            
#         ans = 0
#         left, right = 0, len(height) - 1
#         left_max, right_max = height[left], height[right]
        
#         while left < right:
#             # The smaller boundary wall dictates the water level constraint
#             if left_max < right_max:
#                 left += 1
#                 left_max = max(left_max, height[left])
#                 ans += left_max - height[left]
#             else:
#                 right -= 1
#                 right_max = max(right_max, height[right])
#                 ans += right_max - height[right]
                
#         return ans

if __name__=="__main__":
    sol=Solution()
    # height=[0,1,0,2,1,0,1,3,2,1,2,1]
    height=[4,2,0,3,2,5]
    # height = [4,2,3]
    print(sol.trap(height))
