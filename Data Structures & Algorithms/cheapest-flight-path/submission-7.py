class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # NOTE: flights is not guaratneed to be ordered...
        # set unreachable destinations for all nodes except src
        # -> this means 1 breadth/level is known (meaning 0 hops allowed)
        # for i in range(k+1): update weights based on Bellman-Ford dist. eq.
        # -> min(curr_price_2_src + curr_price_src_2_dest, curr_price_2_dest)
        # we keep track of final_prices array
        # while updating neighbors, don't update final_prices arr immediately
        length=len(flights)
        prices=[math.inf for i in range(n)]
        prices[src]=0
        for i in range(k+1):
            temp=prices.copy()
            for s,d,p in flights:
                if prices[s]==math.inf: 
                    # print("skipped\n")
                    continue
                temp[d]=min(prices[s]+p, temp[d])
                # print(f"s,d,p:{s},{d},{p}")
                # print(f"prices[s]+p:{prices[s]}+{p}={prices[s]+p}")
                # print(f"prices[d]:{prices[d]}")
                # print(f"temp:{temp}\n")
            prices=temp
        return -1 if prices[dst]==math.inf else prices[dst]
        

            



        

        