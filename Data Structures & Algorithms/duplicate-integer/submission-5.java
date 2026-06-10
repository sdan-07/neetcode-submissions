class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Integer>map=new HashMap<>();

        for(int val:nums){
            map.put(val, map.getOrDefault(val,0)+1);
        }

        for(int count:map.values()){
            if(count>1){
                return true;
            }
        }
        return false;
    }
}