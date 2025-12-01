public class Solution {
    public IList<IList<string>> GroupAnagrams(string[] strs) {
        var groupAnagram = new Dictionary<string, List<string>>();
        for(int i = 0 ; i < strs.Length; i++){
            string currentWord = strs[i];
            //Make a list of the chars in this word
            var charList = new List<char>();
            for(int j = 0; j < currentWord.Length; j++){
                charList.Add(currentWord[j]);
            }
            // Now we need to sort this list
            charList.Sort();
            // Make this sorted list into a string
            string sortedString = new string(charList.ToArray());
            // Add to the main dict the sorted list and the words with that
            if(!groupAnagram.ContainsKey(sortedString)){
                // Create empty list value for the new sorted word found
                groupAnagram[sortedString] = new List<string>();
            }
            //Add the word associated with this sorted list 
            groupAnagram[sortedString].Add(currentWord);
            
        }
        var result = new List<IList<string>>();

        foreach (var list in groupAnagram.Values)
        {
            result.Add(list);  // list is List<string> which is valid for IList<string>
        }

        return result;
    }
}