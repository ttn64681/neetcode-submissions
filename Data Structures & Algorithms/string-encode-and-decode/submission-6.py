class Solution:
    # prepend each str w/ delimiter + length and combine
    def encode(self, strs: List[str]) -> str:
        encoded = "".join([f'{len(s)}#{s}' for s in strs])
        print(encoded)
        return encoded

    # expect delimiter, iterate over (length) chars to extract
    def decode(self, s: str) -> List[str]:
        suffix=[] # stores integers for word_len
        word_len=-1 # convert suffix to int
        decoded=[]
        i=0

        # Total Time -> O(n*k + n)
        while i < len(s): # O(n)
            # check delimiter + append
            if len(suffix)==0:
                while s[i] != '#':
                    suffix.append(s[i])
                    i+=1
                word_len=int("".join(suffix)) #O(k+k)
                i+=1

            # else add char
            else:
                if word_len==0:
                    decoded.append("")
                    print(f'decoded when #0 -> {decoded}')
                else:   
                    word=[]
                    for j in range(word_len):
                        word.append(s[i])
                        i+=1
                    decoded.append("".join(word)) # O(n)
                suffix=[] # reset
        
        # edge case if word_len == 0
        if word_len==0:
            decoded.append("")
            print(f'decoded when #0 -> {decoded}')
        return decoded