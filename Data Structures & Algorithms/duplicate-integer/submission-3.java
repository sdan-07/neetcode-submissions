//import java.util.Arrays;
class Solution {
    public boolean hasDuplicate(int[] nums) {
        int count=0;
        Arrays.sort(nums);
        for(int i=0; i<nums.length; i++){
            if(i != nums.length-1){
                if(nums[i]==nums[i+1]){
                    count++;
                }
            }
            
        }
        if(count > 0){
            return true;
        }
        return false;
    }
}