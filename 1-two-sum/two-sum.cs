public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        //This will hold the number : location pair
        var dict = new Dictionary<int, int>();
        for(int i = 0; i < nums.Length; i++){
            int compliment = target - nums[i];
            if(dict.ContainsKey(compliment)){
                int[] returnNums = new int[] {i, dict[compliment]};
                return returnNums;
            }
            // Put the number as key and the value as the position
            dict[nums[i]] = i;
        }
        return null;
    }
}