class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 2:30pm - 
        # 1st_day is buy, 2nd_day is sell
        # profit = 2nd_day - 1st_day
        # if profit = 0 or <0, return 0
        ## (when there is no bigger right number)

        # ideally want to first pick smallest number to left,
        # then pick biggest number to right compared to first pick
        
        # brute force:
        # for each number, find biggest number to right of it and
        # calc the profit

        # postfix max arr:
        # calc max number to the right of each index
        # then do 1 pass to calc profit based on max right num
        n=len(prices)
        profit=0
        max_right=[0]*n # [0,0,0,0,0,0]
        curr_max_right=0
        for i in range(n-1,-1,-1):
            max_right[i]=curr_max_right
            curr_max_right=max(prices[i], curr_max_right)
        # [0,0,0,0,0,0], curr_max_right= 1
        # [0,0,0,0,1,0], curr_max_right= 7
        # [0,0,0,7,1,0], curr_max_right= 7
        # [0,0,7,7,1,0], curr_max_right= 7
        # [0,7,7,7,1,0], curr_max_right= 7
        # [7,7,7,7,1,0], curr_max_right= 10
        # print(max_right)
        for i,p in enumerate(prices):
            curr_profit=max_right[i]-p
            profit=max(curr_profit, profit)
        # 10: curr_profit= 7-10= 0
        # 1: curr_profit= 7-1= 6
        # 5: curr_profit= 7-5= 2
        # 6: curr_profit= 7-6= 1
        # 7: curr_profit= 1-7= 0
        # 8: curr_profit= 0-1= 0
        return profit
        # test cases:
