public class Solution {
    public bool IsAnagram(string s, string t) {
        // This is just checking frequenct of char in a string 
        // We can create 2 dictionarys of strings and char freq
        // If both these dictionaries match then we have an anagram 
        var freqDictS = new Dictionary<char, int>();
        var freqDictT = new Dictionary<char, int>();
        for(int i = 0; i < s.Length; i++){
            if(!freqDictS.ContainsKey(s[i])){
                freqDictS[s[i]] = 1;
            }
            else{
                freqDictS[s[i]]++;
            }
        }
        for(int i = 0; i < t.Length; i++){
            if(!freqDictT.ContainsKey(t[i])){
                freqDictT[t[i]] = 1;
            }
            else{
                freqDictT[t[i]]++;
            }
        }
        return freqDictT.Count == freqDictS.Count && !freqDictT.Except(freqDictS).Any();
       
    }
}