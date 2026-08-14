class Solution:

    def encode(self, strs: List[str]) -> str:
        # ["Hello", "World"] -> "5#Hello5#World"
        # length, delimiter prefix
        # count each word, append len in front, join with # delimiter
        encode_str=[]
        for i in range(len(strs)):
            encode_str.append(str(f"{len(strs[i])}#{strs[i]}"))
        encode_str=''.join(encode_str)
        # print(f"encode_str: {encode_str}")
        return encode_str

    def decode(self, s: str) -> List[str]:
        # "5#Hello5#World" -> ["Hello", "World"]
        # length, delimiter prefix (loop until first # is read to get the length)
        # sliding window? then read until next # and store, repeat until end of string
        decode_arr=[]
        i=0
        while i < len(s):
            decode_buffer=[]
            len_buffer=[]
            while s[i]!="#":
                len_buffer.append(s[i])
                i+=1
            i+=1
            length=''.join(len_buffer)
            # print(int(length))
            for j in range(int(length)):
                decode_buffer.append(s[i])
                i+=1
            decode_str=''.join(decode_buffer)
            decode_arr.append(decode_str)
            # print(f"decode_arr: {decode_arr}")
        return decode_arr