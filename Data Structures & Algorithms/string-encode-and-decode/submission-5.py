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

        # '#0
        # 1. suffix=[]
        # 1. suffix=[#]
        # 2. suffix=[#,0], i==2
        # 3. decoded=["Hello"]
        while i < len(s):
            # check delimiter + append
            if len(suffix)==0:
                while s[i] != '#':
                    suffix.append(s[i])
                    i+=1
                word_len=int("".join(suffix))
                i+=1

            # else add char
            else:
                word=[]
                for j in range(word_len):
                    word.append(s[i])
                    i+=1
                decoded.append("".join(word))
                suffix=[] # reset
        
        # edge case if word_len == 0
        if word_len==0:
            decoded.append("")
            print(f'decoded when #0 -> {decoded}')
        return decoded