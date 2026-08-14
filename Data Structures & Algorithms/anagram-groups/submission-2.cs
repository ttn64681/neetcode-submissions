public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        Dictionary<string, List<string>> hashMap = new Dictionary<string, List<string>>();
        

        foreach (string x in strs) {
            char[] chars = x.ToArray(); // turn string to char array
            Array.Sort(chars);
            string str = new string(chars);

            if (!hashMap.ContainsKey(str)) {
                hashMap.Add(str, new List<string>() {x}); // add at key value string[] w/ element in it
            } else {
                hashMap[str].Add(x);
            }
        }

        List<List<string>> resList = new List<List<string>>();

        foreach (var item in hashMap) { // iterate thru all pairs
            resList.Add(item.Value);
        }

        return resList;
    }
}
