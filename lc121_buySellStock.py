class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l=0
        r=l+1
        n=len(prices)
        least_left=l
        max_right=r
        max_profit=0
        while r<n:
            if prices[l]<prices[least_left]:
                least_left=l
                max_right=r
            if prices[r]>prices[max_right]:
                max_right=r
            profit=prices[max_right]-prices[least_left]
            if profit>max_profit:
                max_profit=profit
            l+=1
            r+=1
        return max_profit

 
if __name__=="__main__":
    sol=Solution()
    # prices1=[1,4,2]
    # prices2=[7,1,5,3,6,4]
    # prices3=[7,6,4,3,1]
    # prices4=[2,1,4]
    # print(sol.maxProfit(prices1))
    # print(sol.maxProfit(prices2))
    # print(sol.maxProfit(prices3))
    # print(sol.maxProfit(prices4))
    print(sol.maxProfit([10, 11, 1, 3]))


# better Solution
# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:
#         if not prices:
#             return 0
            
#         min_price = float('inf')
#         max_profit = 0
        
#         for price in prices:
#             # Step 1: Constantly lock in the cheapest buying opportunity seen so far
#             if price < min_price:
#                 min_price = price
#             # Step 2: If today's price isn't a new low, check what our profit would be if we sold today
#             elif price - min_price > max_profit:
#                 max_profit = price - min_price
                
#         return max_profit


