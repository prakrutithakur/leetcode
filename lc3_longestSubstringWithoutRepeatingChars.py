class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tracingObj={}
        max_length=0
        l=0
        r=0
        while r<=len(s)-1:
            if s[r] in tracingObj:
                new_left=tracingObj[s[r]]+1
                if new_left>l:
                    l=tracingObj[s[r]]+1
            tracingObj[s[r]]=r
            current_length=r-l+1
            if current_length>max_length:
                max_length=current_length
            r+=1
        return max_length 


if __name__ == "__main__":
    sol=Solution()
    user_string=input("Enter the string: ")
    print(sol.lengthOfLongestSubstring(user_string))