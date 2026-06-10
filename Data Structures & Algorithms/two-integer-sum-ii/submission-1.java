class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int diff = 0, sum =0,left=0, right = numbers.length-1;

        while(left < right){
            sum = numbers[left] + numbers[right];
            if(sum > target){
                right--;
            }else if(sum == target){
                return new int[]{(left+1),(right+1)};
            }else{
                left++;
            }
        }

        return new int[0];
    }
}
