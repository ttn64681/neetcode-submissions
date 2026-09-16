class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest=''
        n=len(s)
        left,right=0,0
        if len(s)==1: return s

        # a b a c
        # ^     ^
        # c a b a
        # ^     ^
        # how to choose which pointer moves inwards?

        # hard to choose in cases like a b a a

        # instead, a guaranteed way is to start from the center and check left and right
        # but then what about abbc? this ^ way requires odd length palindrome, not even
        # my solution: have two functions that check for odd and even each character...

        def helper_odd(i):
            beg,end=i,i
            l,r=i-1,i+1
            while l>=0 and r<n:
                if s[l]==s[r]:
                    beg,end=l,r
                    l-=1
                    r+=1
                else:
                    break
            return ''.join(s[beg:end+1])

        def helper_even(i):
            beg,end=i,i+1
            l,r=beg,end
            if r>=n: return ''
            elif s[l]!=s[r]: return ''
            while l>=0 and r<n:
                if s[l]==s[r]:
                    beg,end=l,r
                    l-=1
                    r+=1
                else:
                    break
            return ''.join(s[beg:end+1])

        for i in range(n):
            pal_odd = helper_odd(i)
            pal_even = helper_even(i)
            # print(f"pal_odd: {pal_odd}, pal_even: {pal_even}\n")
            pal = pal_even if len(pal_even)>len(pal_odd) else pal_odd
            if len(pal)>len(longest): longest=pal

        return longest
                
                    

        