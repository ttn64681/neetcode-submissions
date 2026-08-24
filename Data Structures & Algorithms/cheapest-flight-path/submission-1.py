class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Bellman-Ford updates breadth by breadth. First update means you only
        # see the src and the src's immediate neighbors (so no intermed. hops)
        # So if we cap the loop to k+1 (since k=0 means we still need to loop
        # once). every other breadth is unreachable (infinity) from src.

        # for k hops, check each flight:
        # if flight's price from src [0]+ curr price [2] > price to dest [1]
        # set that new price as official src-to-dest price
        s2d_prices=[math.inf for i in range(n)]
        s2d_prices[src]=0
        
        for i in range(k+1): #k=0 hops means run once O(k)
            cpy=s2d_prices.copy() # essential to track current min dest prices
            # print(f"{i}'th loop: {s2d_prices}")
            for s,d,p in flights: # update edges each run O(E)
                if s==math.inf: continue
                # print(f"flight[{s},{d},{p}]")
                if s2d_prices[s] + p < cpy[d]: # keep og src, but update curr min dest price
                    cpy[d] = s2d_prices[s] + p
                    # print(f"new min price of {d} instead of {s2d_prices[d]}: {s2d_prices[s]}+{p}={cpy[d]}")
            s2d_prices=cpy
        return s2d_prices[dst] if s2d_prices[dst] != math.inf else -1



        

        