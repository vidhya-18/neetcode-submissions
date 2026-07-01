class Solution {
    public int[] twoSum(int[] nums, int target) {
    HashMap<Integer,Integer>  mpp = new HashMap<>();
    int[] arr = new int[2];
    for(int i=0;i<nums.length;i++)
    {
        Integer sum = target - nums[i];
        if(mpp.containsKey(sum)  && i!=mpp.get(sum))
        {
            arr[0]=mpp.get(sum);
            arr[1]=i;
        } 
        mpp.put(nums[i],i);
    }
    return arr;
    }
}
