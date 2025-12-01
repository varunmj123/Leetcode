public class Solution {
    public bool ContainsDuplicate(int[] nums) {
        var seenNumbers = new Dictionary<int,int>();
        for(int i = 0; i < nums.Length; i++){
            if(seenNumbers.ContainsKey(nums[i])){
                return true; 
            }
            seenNumbers[nums[i]] = i;
        }
        return false;
    }
}