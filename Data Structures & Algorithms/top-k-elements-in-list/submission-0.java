class Solution {
    public int[] topKFrequent(int[] nums, int k) {  
    HashMap <Integer,Integer> mpp = new HashMap<>();
    for(int i=0;i<nums.length;i++)
    {
        mpp.put(nums[i],mpp.getOrDefault(nums[i],0)+1);
    }  
    HashMap <Integer,List<Integer>> reverseMap= new HashMap<>();
    for(int num : mpp.keySet())
    {
        int count=mpp.get(num);
        if(!reverseMap.containsKey(count))
         reverseMap.put(count,new ArrayList<Integer>());
        reverseMap.get(count).add(num); 
    }
    int[] res=new int[k];
    int ind=0;
    for(int possiblecount=nums.length;possiblecount>=1;possiblecount--)
    {
        if(reverseMap.containsKey(possiblecount))
        {
            for(int n:reverseMap.get(possiblecount))
            {
                if(ind<k)res[ind++]=n;
                else break;
            }
        }
        if(ind>=k)break;
    }
    return res;
    }
}
