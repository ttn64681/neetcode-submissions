class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for x in strs:
                encoded += x + "€" 
            
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        array = list(s) # char array
        print(array)
        currStr = ""
        resArray = []
        for x in array:
            if x == "€":
                resArray.append(currStr)
                currStr = ""
            else:
                currStr += x

        return resArray